import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Board from "./pages/Board";
import Projects from "./pages/Projects";
import MyTasks from "./pages/MyTasks";
import Navbar from "./components/Navbar";
import { getToken, logout } from "./api/auth";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(!!getToken());

  const handleLogout = () => {
    logout();
    setLoggedIn(false);
  };

  return (
    <Router>
      {loggedIn ? (
        <div>
          <Navbar onLogout={handleLogout} />

          <Routes>
            <Route path="/" element={<Board />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/my-tasks" element={<MyTasks />} />
          </Routes>
        </div>
      ) : (
        <Routes>
          <Route path="*" element={<Login onLogin={() => setLoggedIn(true)} />} />
        </Routes>
      )}
    </Router>
  );
}
