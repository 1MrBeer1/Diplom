import React, { useState } from "react";
import { login } from "../api/auth";
import "../index.css"; // чтобы тёмная тема применялась

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);
      onLogin();
    } catch (err) {
      setError("Неверное имя пользователя или пароль");
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <h1 className="login-logo">KANBAN FLOW</h1>
        <form onSubmit={handleSubmit} className="login-form">
          <h2>Вход в систему</h2>

          <input
            placeholder="Имя пользователя"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            placeholder="Пароль"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {error && <p className="error">{error}</p>}

          <button type="submit">Войти</button>
        </form>
        <p className="login-footer">© 2025 Kanban Flow — All rights reserved</p>
      </div>
    </div>
  );
}
