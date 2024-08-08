import React, { useState } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "./firebase";
import earthquake from "../earthquake.png"

import { Link, useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const logIn = (e) => {
    e.preventDefault();
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredintial) => {
        console.log(userCredintial);
        navigate("/notification");
      })
      .catch((error) => {
        console.log(error);
        alert(error);
      });
  };
  return (
    <>
    <div className="logo">
    <img src={earthquake} alt="Logo" />
    <h3>Shaky</h3>
    </div>
    
    <div className="main">
      
      <div className="img"></div>
      
      <div className="login">
      
        <h1>Login</h1>
        <div className="log">
        
        <form action="#" onSubmit={logIn}>
          <div className="detail">
          
          <h3>Login to your account</h3>
            <label for="e-mail">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Enter your e-mail"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <label for="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Enter your password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)
              }
            />
            <button type="submit">Log In</button>
            <div className="click">
              <p>Don't have an account?</p>
              <Link  to="/signup">SignUp</Link>
            </div>
          </div>
        </form>
        </div>
      </div>
    </div>
    </>
  );
}

export default Login;
