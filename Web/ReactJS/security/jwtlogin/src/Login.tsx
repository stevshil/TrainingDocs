import React, { useState, startTransition } from "react";
import { login } from "./api";
import { useToken } from "./TokenContext";

const Login: React.FC = () => {
  const { setToken } = useToken();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = () => {
    startTransition(async () => {
      try {
        const data = await login(username, password);
        setToken(data.token);
      } catch {
        setError("Login failed");
      }
    });
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login</h2>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      /><br/>

      <input
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      /><br/>

      <button onClick={handleLogin}>Login</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default Login;
