import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/auth/";

export async function login(username, password) {
  const response = await axios.post(`${API_URL}login/`, { username, password });
  localStorage.setItem("access", response.data.access);
  localStorage.setItem("refresh", response.data.refresh);

  // Получаем роль
  const userRes = await axios.get(`${API_URL}me/`, {
    headers: { Authorization: `Bearer ${response.data.access}` },
  });
  localStorage.setItem("role", userRes.data.role);
  localStorage.setItem("username", userRes.data.username);

  return userRes.data;
}

export function logout() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  localStorage.removeItem("role");
  localStorage.removeItem("username");
}

export function getToken() {
  return localStorage.getItem("access");
}

export function getUserRole() {
  return localStorage.getItem("role");
}

export function getUsername() {
  return localStorage.getItem("username");
}
