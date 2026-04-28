import React, { useEffect, useState } from "react";
import { fetchUsers } from "./api";
import { useToken } from "./TokenContext";

const Users: React.FC = () => {
  const { token } = useToken();
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    if (!token) return;

    let mounted = true;

    fetchUsers(token).then((data) => {
      if (mounted) setUsers(data);
    });

    return () => {
      mounted = false;
    };
  }, [token]);

  return (
    <div style={{ padding: 20 }}>
      <h2>All Users</h2>
      <ul>
        {users.map((u) => (
          <li key={u.username}>
            {u.username} — {u.password}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
