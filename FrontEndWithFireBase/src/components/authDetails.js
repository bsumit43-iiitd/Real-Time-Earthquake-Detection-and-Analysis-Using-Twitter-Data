import React, { useState,useEffect } from 'react';
import { auth } from './firebase';
import { onAuthStateChanged, signOut } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';


function AuthDetails() {
    const [user,setUser] = useState(null);
    const navigate = useNavigate();
    

    useEffect(() => {
        const listen = onAuthStateChanged(auth, (user) => {
            if (user) {
                setUser(user);
            } else {
                setUser(null);
            }
        })
    },[]);

    const userSignOut = () => {
        signOut(auth).then(() => {
            console.log("Sign out successful");
            navigate("/login");

        }).catch(error => console.log(error))
    }
  return (
    <div className='auth'> {user ? <><p>{`Signed In as ${user.email}`}</p> <button onClick={userSignOut}>Sign Out</button>  </> : <p>Signed Out</p> }</div>
  )
}

export default AuthDetails;