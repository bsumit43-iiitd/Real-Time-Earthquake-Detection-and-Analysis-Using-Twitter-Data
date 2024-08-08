from transformers import BertTokenizer, BertForSequenceClassification
import torch
import numpy as np
import locationtagger
import nltk
import emoji
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
 
# essential entity models downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('stopwords')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')


device = torch.device('cpu')

model = BertForSequenceClassification.from_pretrained('model')
model = model.to(device)


tokenizer = BertTokenizer.from_pretrained(
    'bert-base-uncased',
    do_lower_case = True
    )


def dropnull(df):
  df=df.dropna()
  return df

def replaceemoji(df):
    i=0
    for j in df['text']:
        df.at[i,'text'] = emoji.demojize(j)
        i+=1
    return df


def removeurl(df):
    for i in range(0,len(df)):
        df.at[i,'text']=re.sub(r'http\S+', '',df.at[i,'text'], flags=re.MULTILINE)
    return df

def to_lower_case(df):
    for i in range(0,len(df)):
        df.at[i,'text']= df.at[i,'text'].lower()
    return df

def remove_punctuation(df):
    for i in range(0,len(df)):
        df.at[i,'text']= df.at[i,'text'].translate(str.maketrans('', '', string.punctuation))
    return df

def remove_stopwords(df):
    for i in range(0,len(df)):
        word=df.iloc[i]['text']
        word_tokens=word_tokenize(word)
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        for j in filtered_sentence:
            df.at[i,'text']+=" "+str(j)
    return df


def preprocess(df):
    df = dropnull(df)
    df = replaceemoji(df)
    df = to_lower_case(df)
    df = remove_punctuation(df)
    df = remove_stopwords(df)
    return df


def preprocessing(input_text, tokenizer):
  return tokenizer.encode_plus(
                        input_text,
                        add_special_tokens = True,
                        max_length = 32,
                        pad_to_max_length = True,
                        return_attention_mask = True,
                        return_tensors = 'pt'
                   )




def fetchLocations(df):
    l=['countries','region_cities', 'cities','country_regions','country_cities','other_countries',
        'region_cities','other_regions']
    # initializing sample text
    locations=[]
    # extracting entities.
    for i in range (0,df.shape[0]):
        place_entity = locationtagger.find_locations(text = df.iloc[i]['text'])
        for j in range(0,len(l)):
            d=eval('place_entity'+'.'+l[j])
            if isinstance(d, list):
                locations=locations+d
            elif isinstance(d, dict):
                for key, value in d.items():
                    locations.append(key)
    return locations


def predict(df):
    test_ids = []
    test_attention_mask = []
    if(df.empty):
        return []
    else:
        df = preprocess(df)
        for sentence in df['text']:
            encoding = preprocessing(sentence, tokenizer)
            test_ids.append(encoding['input_ids'])
            test_attention_mask.append(encoding['attention_mask'])
        test_ids = torch.cat(test_ids, dim=0)
        test_attention_mask = torch.cat(test_attention_mask, dim=0)
        # Forward pass, calculate logit predictions
        with torch.no_grad():
            output = model(test_ids.to(device), token_type_ids = None, attention_mask = test_attention_mask.to(device))
        predictions = np.argmax(output.logits.cpu().numpy(), axis=1)
        predicted_classes = [pred  for pred in predictions]
        df['Predicted Class'] = predicted_classes
        df = df.drop(df.loc[df['Predicted Class']==0].index)
        locations = fetchLocations(df)
        return(locations)


# print(predict())