import React from "react";
import { Link } from "react-router-dom";

export default function Navbar({ onLogout }) {
  return (
    <nav style={{ display: "flex", gap: "10px", padding: "10px", background: "#eee" }}>
      <Link to="/">Dashboard</Link>
      <Link to="/projects">Projects</Link>
      <Link to="/my-tasks">My Tasks</Link>
      <button onClick={onLogout} style={{ marginLeft: "auto" }}>Выйти</button>
    </nav>
  );
}
