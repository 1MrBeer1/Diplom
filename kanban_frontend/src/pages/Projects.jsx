import React, { useEffect, useState } from "react";
import { fetchProjects } from "../api/tasks"; // или api/projects.js
import { useNavigate } from "react-router-dom";
import { getUserRole } from "../api/auth";

function EmptyProjects() {
  return (
    <div style={{
      padding: 28, borderRadius: 12, background: "var(--bg-secondary)",
      display: "flex", flexDirection: "column", alignItems: "center", gap: 10
    }}>
      <h3 style={{ color: "var(--text-muted)", margin: 0 }}>Проектов пока нет</h3>
      <p style={{ color: "var(--text-muted)", margin: 0 }}>Создай первый проект и начни планирование</p>
    </div>
  );
}

export default function Projects() {
  const [projects, setProjects] = useState(null);
  const navigate = useNavigate();
  const role = getUserRole();

  useEffect(() => {
    let mounted = true;
    fetchProjects().then((res) => { if (mounted) setProjects(res); }).catch(() => { if (mounted) setProjects([]); });
    return () => { mounted = false; };
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 18 }}>
        <h2>Projects</h2>

        {(role === "CEO" || role === "Admin") && (
          <div>
            <button className="primary-btn" onClick={() => navigate("/projects/create")}>Create project</button>
          </div>
        )}
      </div>

      {Array.isArray(projects) && projects.length === 0 && <EmptyProjects />}

      {Array.isArray(projects) && projects.length > 0 && (
        <div style={{ display: "grid", gap: 12 }}>
          {projects.map((p) => (
            <div key={p.id} className="project-card" style={{ padding: 12, borderRadius: 10, background: "var(--card-bg)" }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <strong style={{ color: "var(--text-main)" }}>{p.name}</strong>
                <button onClick={() => navigate(`/projects/${p.id}`)} className="secondary-btn">Open</button>
              </div>
              <p style={{ color: "var(--text-muted)", marginTop: 8 }}>{p.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
