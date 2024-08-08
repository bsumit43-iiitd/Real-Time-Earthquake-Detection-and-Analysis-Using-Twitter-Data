FROM node:alpine

COPY . /ir
WORKDIR /ir/
EXPOSE 8002
RUN npm i
RUN npm run build
RUN npm install -g serve

CMD ["serve", "-s", "-l", "8002", "dist/"]

