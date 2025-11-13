import React, { useState } from "react";
import api from "../api/axiosClient.js";
import { useNavigate } from "react-router-dom";

export default function CreateProject() {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("projects/", { name, description });
      navigate("/projects");
    } catch (err) {
      alert("❌ Ошибка при создании проекта: " + JSON.stringify(err.response?.data || err));
    }
  };

  return (
    <div style={{ padding: 24 }}>
      <h2>Create Project</h2>
      <form onSubmit={handleSubmit} style={{ display: "grid", gap: 12, maxWidth: 400 }}>
        <input placeholder="Project name" value={name} onChange={(e) => setName(e.target.value)} required />
        <textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}
