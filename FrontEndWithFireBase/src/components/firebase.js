
import { initializeApp } from "firebase/app";
import {getAuth} from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAUrc617RL81DIftrvkkCOX4VCTbBK1pPQ",
  authDomain: "react-twitter-hotspot.firebaseapp.com",
  projectId: "react-twitter-hotspot",
  storageBucket: "react-twitter-hotspot.appspot.com",
  messagingSenderId: "180124567106",
  appId: "1:180124567106:web:38805ef320d5f7babb4fdb"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth();

export {app,auth};