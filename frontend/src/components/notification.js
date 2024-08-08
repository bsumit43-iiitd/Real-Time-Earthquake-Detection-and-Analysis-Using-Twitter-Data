import React, { useRef, useEffect } from 'react';
import { html } from './otherFile';
import MyComponent from './myComponent';



const Notification = () => {
  
  const iframeRef = useRef(null);

  useEffect(() => {
    const iframe = iframeRef.current;
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
   
    // Write the HTML string to the iframe document
    if(html){
    iframeDoc.open();
    iframeDoc.write(html);
    iframeDoc.close();}
  }, []);

  return (
    <div className="bd">
      <h2>Earthquake Hits </h2>
      <div className="map">
        <iframe title="map" ref={iframeRef} width="100%" height="500px"></iframe>
      </div>
      <MyComponent/>
    </div>
  );
};

export default Notification;
