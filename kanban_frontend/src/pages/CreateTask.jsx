import React, { useState } from "react";
import api from "../api/axiosClient.js";
import { useNavigate } from "react-router-dom";

export default function CreateTask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [projectId, setProjectId] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("tasks/", {
        title,
        description,
        project: projectId || null,
      });

      navigate("/my-tasks");
    } catch (err) {
      alert("❌ Ошибка при создании задачи: " + JSON.stringify(err.response?.data || err));
    }
  };

  return (
    <div style={{ padding: 24 }}>
      <h2>Create Task</h2>
      <form onSubmit={handleSubmit} style={{ display: "grid", gap: 12, maxWidth: 400 }}>
        <input placeholder="Task title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <input placeholder="Project ID (optional)" value={projectId} onChange={(e) => setProjectId(e.target.value)} />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}
