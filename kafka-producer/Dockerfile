FROM node:12.18.2-alpine

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 3002



CMD [ "node","KafkaProducer.js" ]
