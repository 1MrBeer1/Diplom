import React, { useState } from "react";
import { login } from "../api/auth";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await login(username, password);
      // Сохраняем роль и username для фронта
      // В Login.jsx после успешного login()
      localStorage.setItem("username", username);
      localStorage.setItem("role", data.role); // role приходит с бэка: CEO, Admin, Head, Employee

      onLogin();
    } catch (err) {
      setError("Неверный логин или пароль");
    }
  };

  return (
    <div style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      height: "100vh",
      background: "#f7f9fc"
    }}>
      <form 
        onSubmit={handleSubmit} 
        style={{
          background: "#fff",
          padding: "40px",
          borderRadius: "12px",
          boxShadow: "0 4px 20px rgba(0,0,0,0.1)",
          width: "320px",
          textAlign: "center"
        }}
      >
        <h2 style={{ marginBottom: "20px" }}>Вход в Kanban</h2>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <input
          type="text"
          placeholder="Имя пользователя"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "15px",
            borderRadius: "6px",
            border: "1px solid #ccc"
          }}
        />
        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "20px",
            borderRadius: "6px",
            border: "1px solid #ccc"
          }}
        />
        <button
          type="submit"
          style={{
            width: "100%",
            padding: "10px",
            borderRadius: "6px",
            border: "none",
            background: "#007bff",
            color: "#fff",
            fontWeight: "bold",
            cursor: "pointer"
          }}
        >
          Войти
        </button>
      </form>
    </div>
  );
}
