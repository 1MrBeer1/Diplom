import React, { useEffect, useState } from "react";
import { fetchProjects } from "../api/tasks"; // если у тебя есть API для проектов

export default function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    async function loadProjects() {
      try {
        const data = await fetchProjects();
        setProjects(data || []); // если null, используем пустой массив
      } catch (err) {
        console.error("Ошибка при загрузке проектов:", err);
        setProjects([]); // на случай ошибки
      }
    }

    loadProjects();
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      {projects.length === 0 ? (
        <p>Нет проектов</p>
      ) : (
        projects.map((project) => (
          <div key={project.id}>
            <h3>{project.name}</h3>
            <p>{project.description}</p>
          </div>
        ))
      )}
    </div>
  );
}
