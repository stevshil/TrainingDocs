import './App.css';
import { Header } from './components/Header';
import { Main } from './components/Main';
import { BrowserRouter as Router, Routes, Route } from 'react-router';
import { About } from './components/About';
import { Contact } from './components/Contact';
import { MyChart } from './components/MyChart';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/chart" element={<MyChart />} />
      </Routes>
    </Router>
  );
}

export default App;
