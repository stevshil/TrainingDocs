import { Routes, Route, NavLink, Link } from 'react-router'
import './App.css'

function PageNav() {
return (<nav>
    <NavLink to="/">Home</NavLink>&nbsp;
    <Link to="/home2/Steve">Steve</Link>&nbsp;
    <Link to="/home2/Ben">Ben</Link>&nbsp;
    <NavLink to="/about">About</NavLink><br />
</nav>)
};

export default PageNav;