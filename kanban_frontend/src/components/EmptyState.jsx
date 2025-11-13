import React from "react";

export default function EmptyState({ title, subtitle, action }) {
  return (
    <div style={{
      padding: 26, borderRadius: 12, background: "var(--bg-secondary)",
      display: "flex", flexDirection: "column", alignItems: "center", gap: 8
    }}>
      <h3 style={{ color: "var(--text-muted)", margin: 0 }}>{title}</h3>
      <p style={{ color: "var(--text-muted)", margin: 0 }}>{subtitle}</p>
      {action && <div style={{ marginTop: 12 }}>{action}</div>}
    </div>
  );
}
