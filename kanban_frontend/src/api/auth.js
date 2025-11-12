import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/auth/";

export async function login(username, password) {
  const response = await axios.post(`${API_URL}login/`, { username, password });
  localStorage.setItem("access", response.data.access);
  localStorage.setItem("refresh", response.data.refresh);
  return response.data;
}

export function logout() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
}

export function getToken() {
  return localStorage.getItem("access");
}
