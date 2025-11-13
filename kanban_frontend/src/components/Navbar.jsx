import React, { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { getUserRole, getUsername } from "../api/auth";

export default function Navbar({ onLogout }) {
  const navigate = useNavigate();
  const role = getUserRole();
  const username = getUsername() || "User";
  const [menuOpen, setMenuOpen] = useState(false);

  const initial = username.charAt(0).toUpperCase();

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <div
          className="logo"
          onClick={() => navigate("/")}
          title="Перейти на дашборд"
          role="button"
          tabIndex={0}
        >
          KANBAN — FLOW
        </div>

        <NavLink to="/" end className="navlink">
          Dashboard
        </NavLink>

        <NavLink to="/projects" className="navlink">
          Projects
        </NavLink>

        <NavLink to="/my-tasks" className="navlink">
          My Tasks
        </NavLink>

        {/* Менеджмент пользователей — видит CEO и Admin */}
        {(role === "CEO" || role === "Admin") && (
          <NavLink to="/users" className="navlink">
            Users
          </NavLink>
        )}
      </div>

      <div className="navbar-right">
        <div
          className="avatar"
          onClick={() => setMenuOpen((s) => !s)}
          title={username}
        >
          {initial}
        </div>

        {menuOpen && (
          <div className="dropdown" onMouseLeave={() => setMenuOpen(false)}>
            <p style={{ marginBottom: 8, color: "var(--text-muted)" }}>{username}</p>
            <button onClick={() => { onLogout(); navigate("/"); }}>
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
}
