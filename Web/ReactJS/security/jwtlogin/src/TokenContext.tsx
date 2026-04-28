import React, { createContext, useState, useContext } from "react";

interface TokenContextType {
  token: string | null;
  setToken: (token: string | null) => void;
}

const TokenContext = createContext<TokenContextType | undefined>(undefined);

export function TokenProvider({ children }: { children: React.ReactNode }) {
  const [token, setToken] = useState<string | null>(null);

  return (
    <TokenContext.Provider value={{ token, setToken }}>
      {children}
    </TokenContext.Provider>
  );
}

export function useToken() {
  const ctx = useContext(TokenContext);
  if (!ctx) throw new Error("useToken must be used inside TokenProvider");
  return ctx;
};
