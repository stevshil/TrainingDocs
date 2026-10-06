import { useDeferredValue, useEffect, useState } from 'react'
import { AlertTriangle, LoaderCircle, Search } from 'lucide-react'
import { useParams } from 'react-router-dom'
import { categories, isCategory, type CatalogItem, type Category } from '../types/swapi'
import { fetchCatalog } from '../services/swapi'

const featuredFields: Record<Category, string[]> = {
  characters: ['birth_year', 'gender', 'height', 'homeworld'],
  planets: ['climate', 'terrain', 'population', 'diameter'],
  starships: ['model', 'starship_class', 'crew', 'hyperdrive_rating'],
}

const fieldLabels: Record<string, string> = {
  birth_year: 'ERA', gender: 'GENDER', height: 'HEIGHT', homeworld: 'HOMEWORLD',
  climate: 'CLIMATE', terrain: 'TERRAIN', population: 'POPULATION', diameter: 'DIAMETER',
  model: 'MODEL', starship_class: 'CLASS', crew: 'CREW', hyperdrive_rating: 'HYPERDRIVE',
}

const displayValue = (value: unknown) => {
  if (typeof value !== 'string' || !value || value === 'unknown' || value === 'n/a') return '—'
  if (value.startsWith('https://swapi.info/api/')) {
    const segments = value.split('/').filter(Boolean)
    return segments[segments.length - 1] ?? value
  }
  return value
}

const itemId = (item: CatalogItem, index: number) => item.url.match(/\/(\d+)\/?$/)?.[1] ?? String(index + 1)

export function CatalogPage() {
  const { category: categoryParam } = useParams()
  const category = isCategory(categoryParam) ? categoryParam : 'characters'
  const config = categories[category]
  const [items, setItems] = useState<CatalogItem[]>([])
  const [query, setQuery] = useState('')
  const [expandedId, setExpandedId] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [retryKey, setRetryKey] = useState(0)
  const deferredQuery = useDeferredValue(query)

  useEffect(() => {
    const controller = new AbortController()
    setLoading(true)
    setError(null)
    setQuery('')
    setExpandedId(null)

    fetchCatalog(category, controller.signal)
      .then(setItems)
      .catch((reason: unknown) => {
        if (reason instanceof DOMException && reason.name === 'AbortError') return
        setError(reason instanceof Error ? reason.message : 'Unable to reach the galactic archive.')
      })
      .finally(() => {
        if (!controller.signal.aborted) setLoading(false)
      })

    return () => controller.abort()
  }, [category, retryKey])

  const normalizedQuery = deferredQuery.trim().toLowerCase()
  const filteredItems = items
    .map((item, index) => ({ item, id: itemId(item, index) }))
    .filter(({ item }) => !normalizedQuery || JSON.stringify(item).toLowerCase().includes(normalizedQuery))

  return (
    <section className={`catalog-page accent-${config.accent}`} aria-labelledby="page-title">
      <div className="breadcrumb"><span>ARCHIVE</span><span className="crumb-slash">/</span><span>{config.label.toUpperCase()}</span></div>
      <div className="page-heading">
        <div>
          <div className="eyebrow"><span className="eyebrow-line" /> GALACTIC ATLAS <span className="eyebrow-dot">·</span> {config.label.toUpperCase()}</div>
          <h1 id="page-title">{config.label}<span className="title-period">.</span></h1>
          <p className="page-description">{config.description}</p>
        </div>
        <div className="heading-coordinate" aria-hidden="true">
          <span>SECTOR</span><strong>{category === 'characters' ? '01' : category === 'planets' ? '02' : '03'}—{category === 'characters' ? 'C' : category === 'planets' ? 'P' : 'S'}</strong>
          <span>CORE SYSTEMS</span>
        </div>
      </div>

      <div className="catalog-toolbar">
        <div className="result-count" aria-live="polite">
          <span className="count-number">{loading ? '···' : filteredItems.length.toString().padStart(2, '0')}</span>
          <span>RECORDS {normalizedQuery && !loading ? 'FOUND' : 'IN INDEX'}</span>
        </div>
        <label className="search-box">
          <Search size={17} aria-hidden="true" />
          <span className="sr-only">Search {config.label.toLowerCase()}</span>
          <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder={`Search ${config.label.toLowerCase()}...`} />
          {query && <button className="clear-search" type="button" onClick={() => setQuery('')} aria-label="Clear search">×</button>}
        </label>
      </div>

      {loading && <div className="state-panel" role="status"><LoaderCircle className="spin-icon" size={23} /><div><strong>Scanning the archive</strong><span>Receiving {config.label.toLowerCase()} records...</span></div></div>}

      {!loading && error && <div className="state-panel error-panel" role="alert"><AlertTriangle size={22} /><div><strong>Transmission interrupted</strong><span>{error}</span><button className="retry-button" type="button" onClick={() => setRetryKey((current) => current + 1)}>Retry connection</button></div></div>}

      {!loading && !error && filteredItems.length === 0 && <div className="state-panel empty-panel"><Search size={22} /><div><strong>{items.length ? 'No matching records' : 'No records available'}</strong><span>{items.length ? 'Try a different name, world, or detail.' : 'The archive returned an empty index.'}</span></div></div>}

      {!loading && !error && filteredItems.length > 0 && (
        <div className="record-grid">
          {filteredItems.map(({ item, id }, index) => {
            const expanded = expandedId === id
            return (
              <article className={`record-card ${expanded ? 'expanded' : ''}`} key={`${id}-${item.name}`} style={{ animationDelay: `${Math.min(index, 8) * 35}ms` }}>
                <button className="record-main" type="button" aria-expanded={expanded} onClick={() => setExpandedId(expanded ? null : id)}>
                  <span className="record-topline"><span className="record-type">{config.singular.toUpperCase()}</span><span className="record-id">GF—{id.padStart(3, '0')}</span></span>
                  <span className="record-name">{item.name}</span>
                  <span className="record-fields">
                    {featuredFields[category].slice(0, 3).map((field) => (
                      <span className="record-field" key={field}><span>{fieldLabels[field]}</span><strong>{displayValue(item[field as keyof CatalogItem])}</strong></span>
                    ))}
                  </span>
                  <span className="record-bottom"><span>OPEN FIELD NOTES</span><span className="record-chevron">{expanded ? '−' : '+'}</span></span>
                </button>
                {expanded && <div className="record-details">
                  {featuredFields[category].map((field) => <div className="detail-line" key={field}><span>{fieldLabels[field]}</span><strong>{displayValue(item[field as keyof CatalogItem])}</strong></div>)}
                  <div className="detail-line"><span>APPEARANCES</span><strong>{'films' in item ? item.films.length : 0} recorded</strong></div>
                </div>}
              </article>
            )
          })}
        </div>
      )}

      <footer className="catalog-footer"><span>END OF TRANSMISSION</span><span>GALACTIC FIELD GUIDE <i>·</i> {new Date().getFullYear()}</span></footer>
    </section>
  )
}