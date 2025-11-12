import axios from "axios";
import { getToken } from "./auth";

const API_URL = "http://127.0.0.1:8000/api/";

const client = axios.create({
  baseURL: API_URL,
  headers: () => ({
    Authorization: `Bearer ${getToken()}`,
  }),
});

// Получение всех проектов
export async function fetchProjects() {
  const response = await client.get("projects/");
  return response.data;
}

// Получение Kanban по проекту
export async function fetchKanban(projectId) {
  const response = await client.get(`tasks/kanban/${projectId}/`);
  return response.data;
}

// Обновление задач
export async function updateTasksBulk(updates) {
  await client.patch(`tasks/bulk-update/`, updates);
}
