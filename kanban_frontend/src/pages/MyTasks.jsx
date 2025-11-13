import React, { useEffect, useState } from "react";
import { fetchMyTasks } from "../api/tasks";
import { useNavigate } from "react-router-dom";
import { getUserRole } from "../api/auth";
import TaskCard from "../components/TaskCard";



export default function MyTasks() {
  const [tasks, setTasks] = useState(null);
  const navigate = useNavigate();
  const role = getUserRole();

  useEffect(() => {
    fetchMyTasks().then(setTasks).catch(() => setTasks([]));
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 18 }}>
        <h2>My Tasks</h2>
        {(role === "CEO" || role === "Admin" || role.startsWith("Head")) && (
          <button className="primary-btn" onClick={() => navigate("/tasks/create")}>Create task</button>
        )}
      </div>

      {!tasks && <p style={{ color: "var(--text-muted)" }}>Загрузка...</p>}
      {Array.isArray(tasks) && tasks.length === 0 && (
        <div style={{ color: "var(--text-muted)" }}>У вас пока нет задач</div>
      )}

      {Array.isArray(tasks) && tasks.map(t => <TaskCard key={t.id} task={t} />)}
    </div>
  );
}
