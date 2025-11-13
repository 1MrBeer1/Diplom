import api from "axiosClient.js";

export async function fetchProjects() {
  return (await api.get("projects/")).data;
}

export async function fetchKanban(projectId) {
  return (await api.get(`tasks/kanban/${projectId}/`)).data;
}

export async function fetchMyTasks() {
  return (await api.get("tasks/my/")).data;
}

export async function updateTasksBulk(updates) {
  return await api.patch("tasks/bulk-update/", updates);
}
