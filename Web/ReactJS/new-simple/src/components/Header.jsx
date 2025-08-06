import { Link } from 'react-router';

export function Header() {
  return (
    <nav>
      <Link to="/">Home</Link> |{" "}
      <Link to="/about">About</Link> |{" "}
      <Link to="/contact">Contact</Link> |{" "}
      <Link to="/chart">Chart</Link>
    </nav>
  );
}