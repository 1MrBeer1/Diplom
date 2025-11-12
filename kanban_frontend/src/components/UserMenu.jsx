import React, { useState } from "react";

export default function UserMenu({ username, onLogout }) {
  const [open, setOpen] = useState(false);
  const initial = username.charAt(0).toUpperCase();

  return (
    <div style={{ position: "relative" }}>
      <div
        onClick={() => setOpen(!open)}
        style={{
          width: "40px",
          height: "40px",
          borderRadius: "50%",
          background: "#007bff",
          color: "#fff",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          cursor: "pointer",
          fontWeight: "bold",
          userSelect: "none",
        }}
      >
        {initial}
      </div>

      {open && (
        <div
          style={{
            position: "absolute",
            right: 0,
            top: "50px",
            background: "#fff",
            border: "1px solid #ddd",
            borderRadius: "8px",
            padding: "10px",
            minWidth: "160px",
            boxShadow: "0 4px 20px rgba(0,0,0,0.1)",
            zIndex: 100,
          }}
        >
          <p style={{ margin: "0 0 10px 0", fontWeight: "bold" }}>{username}</p>
          <button
            onClick={onLogout}
            style={{
              width: "100%",
              padding: "8px",
              borderRadius: "6px",
              border: "none",
              background: "#ff4d4f",
              color: "#fff",
              cursor: "pointer",
            }}
          >
            Выйти
          </button>
        </div>
      )}
    </div>
  );
}
