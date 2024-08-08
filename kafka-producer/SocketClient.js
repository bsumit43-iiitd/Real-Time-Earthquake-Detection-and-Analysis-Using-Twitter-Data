const io = require("socket.io-client");

const socket = io("http://127.0.0.1:8001", {
  extraHeaders: {
    Authorization: "Bearer ir",
  },
});

socket.on("connect", () => {
  console.log("Connected to server!");
});

socket.on("message", (data) => {
  console.log(data);
});

socket.on("locations", (data) => {
  console.log(data);
});

socket.on("map", (data) => {
  // console.log(data);
});

socket.on("disconnect", (data) => {
  console.log(data);
});
