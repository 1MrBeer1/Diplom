import React from "react";
import { Link } from "react-router-dom";
import UserMenu from "./UserMenu";

export default function Navbar({ onLogout }) {
  const username = localStorage.getItem("username") || "User";
  const role = localStorage.getItem("role") || "Employee";

  return (
    <nav style={{ display: "flex", justifyContent: "space-between", padding: "10px 20px", background: "#f7f9fc", borderBottom: "1px solid #ddd" }}>
      <div style={{ display: "flex", gap: "15px" }}>
  <Link to="/">Dashboard</Link>
  <Link to="/projects">Projects</Link>
  <Link to="/my-tasks">My Tasks</Link>

  {(role === "CEO" || role === "Admin") && (
    <>
      <Link to="/create-project">Создать проект</Link>
      <Link to="/manage-heads">Назначить начальников</Link>
      <Link to="/create-user">Создать пользователя</Link>
      <Link to="/edit-user">Редактировать пользователя</Link>
    </>
  )}

  {role && role.startsWith("Head") && (
    <Link to="/create-task">Создать задачу</Link>
  )}

  {role === "Admin" && <Link to="/system-metrics">Метрики</Link>}
</div>

      <UserMenu username={username} onLogout={onLogout} />
    </nav>
  );
}
