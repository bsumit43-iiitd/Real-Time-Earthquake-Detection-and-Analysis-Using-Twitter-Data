import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  HashRouter,
} from "react-router-dom";
import Login from "./components/login";
import Signup from "./components/signup";
import Notification from "./components/notification";
import NewNotification from "./components/newNotification";

function App() {
  return (
    <HashRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<Login />} />
          <Route path="/notification" element={<Notification />} />
          <Route path="/newnotification" element={<NewNotification />} />
        </Routes>
    </HashRouter>
  );
}

export default App;
