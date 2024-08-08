import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import Notification from "./notification";

function MyComponent() {
  const [message, setMessage] = useState("");
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    const socket = io("http://127.0.0.1:8001", {
      extraHeaders: {
        Authorization: "Bearer ir",
      },
    });

    socket.on("connect", () => {
      console.log("Connected to server!");
    });

    socket.on("message", (data) => {
      setMessage(data);
      console.log(data);
    });

    socket.on("locations", (data) => {
      setLocations(data);
      console.log(data);
      
    });

    socket.on("disconnect", (data) => {
      console.log(data);
      
    });

    // Return a cleanup function to close the socket when the component unmounts
    return () => {
      socket.disconnect();
    };
  }, []);
  return (
    <div>
      <div>Message: {message}</div>
      
      
      <ul>
        Locations:{locations}
        {/* {locations.map((location, index) => (
          <li key={index}>{location}</li>
        ))} */}
      </ul>
      
    </div>
  );
}

export default MyComponent;