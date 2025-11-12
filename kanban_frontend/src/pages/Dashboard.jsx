import React, { useEffect, useState } from "react";
import KanbanBoard from "../components/KanbanBoard";
import Projects from "./Projects";
import MyTasks from "./MyTasks";
import { getToken } from "../api/auth";
import axios from "axios";

export default function Dashboard() {
  const [view, setView] = useState("kanban"); // "kanban" | "projects" | "my-tasks"
  const [userRole, setUserRole] = useState("user"); 
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    async function fetchUser() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/auth/me/", {
          headers: { Authorization: `Bearer ${getToken()}` },
        });
        setUserRole(res.data?.role || "user"); // безопасная проверка role
      } catch {
        setUserRole("user");
      }
    }

    async function fetchProjects() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/projects/", {
          headers: { Authorization: `Bearer ${getToken()}` },
        });
        setProjects(res.data || []); // если данных нет, пустой массив
      } catch {
        setProjects([]);
      }
    }

    fetchUser();
    fetchProjects();
  }, []);

  return (
    <div>
      <nav style={{ display: "flex", gap: "20px", padding: "10px", background: "#eee" }}>
        <button onClick={() => setView("kanban")}>Kanban</button>
        <button onClick={() => setView("projects")}>Projects</button>
        <button onClick={() => setView("my-tasks")}>My Tasks</button>
      </nav>

      {view === "kanban" && <KanbanBoard projectId={null} showEmptyColumns={true} />}

      {view === "projects" && <Projects userRole={userRole} projects={projects} />}

      {view === "my-tasks" && <MyTasks />}
    </div>
  );
}
