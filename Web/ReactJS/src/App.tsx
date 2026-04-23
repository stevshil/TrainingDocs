import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router";
import Home from "./Home";
import About from "./About";
import PageNav from './PageNav';
import Error from './Error';
import Home2 from './Home2';

function App() {
  return (
    <Router>
      <PageNav />
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />
        <Route path="/home2/:name" element={<Home2 />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<Error />} />
      </Routes>
    </Router>
  );
};

export default App;