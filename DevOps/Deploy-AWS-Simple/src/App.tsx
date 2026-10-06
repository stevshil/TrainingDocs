import { Navigate, Route, Routes } from 'react-router-dom'
import { SiteShell } from './components/SiteShell'
import { CatalogPage } from './pages/CatalogPage'

export default function App() {
  return (
    <SiteShell>
      <Routes>
        <Route path="/" element={<Navigate to="/characters" replace />} />
        <Route path="/:category" element={<CatalogPage />} />
        <Route path="*" element={<Navigate to="/characters" replace />} />
      </Routes>
    </SiteShell>
  )
}