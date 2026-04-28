import React, { Suspense } from "react";
import { TokenProvider, useToken } from "./TokenContext";
import Login from "./Login";
import Users from "./Users";

export function AppContent() {
  const { token } = useToken();

  return (
    <Suspense fallback={<p>Loading...</p>}>
      {token ? <Users /> : <Login />}
    </Suspense>
  );
};

export function App() {
  return (
    <TokenProvider>
      <AppContent />
    </TokenProvider>
  )
};

export default App;
