import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../api/auth";

export default function UsersList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const token = getToken();
        const res = await axios.get("/api/users/", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUsers(res.data);
      } catch (err) {
        console.error("Ошибка загрузки пользователей:", err);
      }
    };
    fetchUsers();
  }, []);

  return (
    <div className="users-page">
      <h2>Пользователи</h2>
      {users.length === 0 ? (
        <p>Нет зарегистрированных пользователей</p>
      ) : (
        <table className="users-table">
          <thead>
            <tr>
              <th>Имя пользователя</th>
              <th>Email</th>
              <th>Роль</th>
              <th>Отдел</th>
            </tr>
          </thead>
          <tbody>
            {users.map((u) => (
              <tr key={u.id}>
                <td>{u.username}</td>
                <td>{u.email}</td>
                <td>{u.role}</td>
                <td>{u.department || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
