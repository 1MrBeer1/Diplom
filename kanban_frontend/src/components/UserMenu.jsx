import React, { useState } from "react";
import { logout, getToken } from "../api/auth";

export default function UserMenu({ username, onLogout }) {
  const [open, setOpen] = useState(false);

  const handleLogout = () => {
    logout();
    onLogout(); // уведомляем App о логауте
  };

  return (
    <div style={{ position: "relative", display: "inline-block" }}>
      {/* Кружок с первой буквой */}
      <div
        onClick={() => setOpen(!open)}
        style={{
          width: "40px",
          height: "40px",
          borderRadius: "50%",
          background: "#4f46e5",
          color: "#fff",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontWeight: "bold",
          fontSize: "18px",
          cursor: "pointer",
          userSelect: "none",
        }}
      >
        {username ? username[0].toUpperCase() : "U"}
      </div>

      {/* Выпадающее меню */}
      {open && (
        <div
          style={{
            position: "absolute",
            right: 0,
            marginTop: "10px",
            background: "#fff",
            border: "1px solid #ddd",
            borderRadius: "8px",
            boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
            minWidth: "160px",
            zIndex: 1000,
          }}
        >
          <div style={{ padding: "10px", fontWeight: "bold" }}>{username}</div>
          <div
            onClick={handleLogout}
            style={{
              padding: "10px",
              borderTop: "1px solid #eee",
              cursor: "pointer",
              color: "#4f46e5",
              fontWeight: "bold",
              textAlign: "center",
            }}
          >
            Logout
          </div>
        </div>
      )}
    </div>
  );
}
