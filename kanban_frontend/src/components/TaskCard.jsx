import React from "react";

export default function TaskCard({ task }) {
  return (
    <div className="task-card">
      <strong>{task.title}</strong>
      <p>{task.description}</p>
      <small>{task.assigned_to_username || "Unassigned"}</small>
    </div>
  );
}
