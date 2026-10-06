import { NavLink } from 'react-router-dom'
import { Orbit, Radio, Telescope } from 'lucide-react'
import { categories, type Category } from '../types/swapi'

const navigation = Object.entries(categories) as [Category, (typeof categories)[Category]][]

export function SiteShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="/characters" aria-label="Galactic Field Guide home">
          <span className="brand-mark"><Orbit size={19} strokeWidth={1.8} /></span>
          <span className="brand-name">GALACTIC <b>FIELD GUIDE</b></span>
        </a>
        <div className="topbar-status"><span className="status-dot" /> ARCHIVE ONLINE <span className="status-divider">/</span> CYCLE 34: ABY
        </div>
        <a className="source-link" href="https://swapi.info/" target="_blank" rel="noreferrer">
          <Telescope size={15} aria-hidden="true" /><span>DATA SOURCE</span>
        </a>
      </header>

      <div className="page-layout">
        <aside className="sidebar" aria-label="Archive navigation">
          <div className="nav-caption">FIELD INDEX <span>03</span></div>
          <nav className="primary-nav">
            {navigation.map(([key, config], index) => (
              <NavLink key={key} to={`/${key}`} className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
                <span className={`nav-index ${config.accent}`}>0{index + 1}</span>
                <span>{config.label}</span>
                <span className="nav-arrow" aria-hidden="true">↗</span>
              </NavLink>
            ))}
          </nav>
          <div className="sidebar-note">
            <div className="note-icon"><Radio size={15} /></div>
            <p>FIELD TRANSMISSION</p>
            <span>Updated from the galactic archive in real time.</span>
          </div>
          <div className="sidebar-footer">A LIVING ATLAS <span>·</span> EST. 1977</div>
        </aside>

        <main className="main-content" id="main-content">{children}</main>
      </div>
    </div>
  )
}