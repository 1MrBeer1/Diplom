import React, { useEffect, useState } from "react";
import { getToken, logout } from "../api/auth";
import axios from "axios";

export default function MyTasks() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchTasks() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/tasks/my-tasks/", {
          headers: { Authorization: `Bearer ${getToken()}` },
        });
        setTasks(res.data || []);
      } catch (err) {
        if (err.response?.status === 401) {
          // Если токен невалидный — автоматически логаут
          logout();
          window.location.reload(); // вернем на страницу логина
        } else {
          console.error(err);
          setTasks([]); // если другая ошибка — просто пустой список
          setError("Не удалось загрузить задачи.");
        }
      }
    }

    fetchTasks();
  }, []);

  if (error) return <div>{error}</div>;
  if (!tasks.length) return <div>У вас нет назначенных задач.</div>;

  return (
    <div>
      <h2>My Tasks</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <strong>{task.title}</strong> — {task.project_name || "Без проекта"}
          </li>
        ))}
      </ul>
    </div>
  );
}
