import React, { useState, useRef, useEffect } from "react";

import io from "socket.io-client";

const NewNotification = () => {
  const iframeRef = useRef(null);

  const [message, setMessage] = useState("");
  const [locations, setLocations] = useState([]);
  const [map, setMap] = useState([]);

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

    socket.on("map", (data) => {
      setMap(() => data);
    //   console.log(data);
    });

    socket.on("disconnect", (data) => {
      console.log(data);
    });

    // Return a cleanup function to close the socket when the component unmounts
    return () => {
      socket.disconnect();
    };
  }, []);


  useEffect(()=>{
    console.log(map)
  },[map])

  useEffect(() => {
    const iframe = iframeRef.current;
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    //alert("Use effect is called");

    // Write the HTML string to the iframe document
    if (map) {
      iframeDoc.open();
      iframeDoc.write(map);
      iframeDoc.close();
    }
  }, [map]);

  return (
    <div className="bd">
      <h2>Earthquake Hit in </h2>
      <div className="map">
        <iframe
          title="map"
          ref={iframeRef}
          width="100%"
          height="500px"
        ></iframe>
      </div>
      <div>Message: {message}</div>

      <ul>
        Locations:{locations.join(", ")}
        
      </ul>
    </div>
  );
};

export default NewNotification;
