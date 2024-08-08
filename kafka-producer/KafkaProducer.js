var fs = require("fs");
const { parse } = require("csv-parse");

var kafka = require("kafka-node");
var Producer = kafka.Producer;
var client = new kafka.KafkaClient("ubuntu:2181/");
var countriesTopic = "tweets",
  KeyedMessage = kafka.KeyedMessage,
  producer = new Producer(client),
  km = new KeyedMessage("key", "message"),
  countryProducerReady = false;

producer.on("ready", function () {
  console.log("Producer for test is ready");
  countryProducerReady = true;
});

producer.on("error", function (err) {
  console.error("Problem with producing Kafka message " + err);
});

var inputFile = "StreamDataSet/test.csv";
var averageDelay = 300;
var spreadInDelay = 200;

var countriesArray;

var parser = parse({ delimiter: "," }, function (err, data) {
  countriesArray = data;
  handleCountry(1);
});

fs.createReadStream(inputFile).pipe(parser);

function handleCountry(currentCountry) {
  var line = countriesArray[currentCountry];
  var country = { id: line[0], event: line[1], source: line[2], text: line[3] };
  produceTestMessage(country);
  var delay = averageDelay + (Math.random() - 0.5) * spreadInDelay;
  if (currentCountry < 96000)
    setTimeout(handleCountry.bind(null, currentCountry + 1), delay);
  else {
    console.log("Hi");
    setTimeout(handleCountry.bind(null, 1), delay);
  }
}

function produceTestMessage(country) {
  (KeyedMessage = kafka.KeyedMessage),
    (countryKM = new KeyedMessage(country.code, JSON.stringify(country))),
    (payloads = [
      {
        topic: countriesTopic,
        messages: countryKM,
        groupId: "ir",
        partition: 0,
      },
    ]);
  if (countryProducerReady) {
    producer.send(payloads, function (err, data) {
      //   console.log(data);
    });
  } else {
    console.error(
      "Test producer is not ready yet, failed to produce message to Kafka."
    );
  }
}
