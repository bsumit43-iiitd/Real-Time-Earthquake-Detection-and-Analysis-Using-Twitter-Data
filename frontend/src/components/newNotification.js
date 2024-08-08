import React, { useState,useRef, useEffect } from 'react';


import io from "socket.io-client";


const NewNotification = () => {
  
  const iframeRef = useRef(null);

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

  useEffect(() => {
    const iframe = iframeRef.current;
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    //alert("Use effect is called");
   
    // Write the HTML string to the iframe document
    if(locations){
    iframeDoc.open();
    iframeDoc.write(locations);
    iframeDoc.close();}
  }, []);

  return (
    <div className="bd">
      <h2>Earthquake Hit in </h2>
      <div className="map">
        <iframe title="map" ref={iframeRef} width="100%" height="500px"></iframe>
      </div>
      <div>Message: {message}</div>
      
      
      <ul>
        Locations:{locations}
        {/* {locations.map((location, index) => (
          <li key={index}>{location}</li>
        ))} */}
      </ul>
     
    </div>
  );
};

export default NewNotification;