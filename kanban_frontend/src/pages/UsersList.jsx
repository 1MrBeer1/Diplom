import React, { useEffect, useState } from "react";
import { fetchUsers } from "../api/users"; // нужно создать API метод

export default function UsersList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers().then(setUsers).catch(console.error);
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h2>Список пользователей</h2>
      <ul>
        {users.map(u => (
          <li key={u.id}>{u.username} - {u.role}</li>
        ))}
      </ul>
    </div>
  );
}
