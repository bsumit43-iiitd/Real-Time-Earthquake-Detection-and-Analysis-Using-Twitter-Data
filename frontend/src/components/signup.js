import React, { useState } from "react";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "./firebase";
import { Link, useNavigate } from "react-router-dom";
import earthquake from "../earthquake.png"

function Signup() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const SignUp = (e) => {
    e.preventDefault();
    createUserWithEmailAndPassword(auth, email, password)
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
        <h1>Sign Up</h1>
        <div className="log">
        <form action="#" onSubmit={SignUp}>
          <div className="detail">
            <h3>Create an account</h3>
            <label for="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              required
              placeholder="Enter new e-mail"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <label for="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              required
              placeholder="Enter new password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit">Sign Up</button>
            <div className="click">
              <p>Already have an account?</p>
              <Link to="/login">Log In</Link>
            </div>
          </div>
        </form>
        </div>
      </div>
    </div>
    </>
  );
}

export default Signup;
