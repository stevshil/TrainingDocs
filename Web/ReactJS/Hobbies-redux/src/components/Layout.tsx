import React from "react";
import { Link, NavLink } from "react-router";
import "../styles/Layout.css";

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="app-shell">
      <header className="app-header">
        <Link to="/" className="logo">
          People Manager
        </Link>
        <nav className="nav">
          <NavLink to="/" className="nav-link">
            Home
          </NavLink>
          <NavLink to="/new" className="nav-link">
            New User
          </NavLink>
        </nav>
      </header>
      <main className="app-main">{children}</main>
      <footer className="app-footer">
        © {new Date().getFullYear()} TPS Services Ltd
      </footer>
    </div>
  );
};

export default Layout;
