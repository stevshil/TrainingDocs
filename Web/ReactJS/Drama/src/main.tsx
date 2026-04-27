import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './components/App.tsx'
import Manual from './Manual'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    {/* <Manual /> */}
  </StrictMode>,
)
