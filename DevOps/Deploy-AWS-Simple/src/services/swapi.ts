import { categories, type CatalogItem, type Category } from '../types/swapi'

const API_BASE_URL = 'https://swapi.info/api'

export async function fetchCatalog(category: Category, signal?: AbortSignal): Promise<CatalogItem[]> {
  const response = await fetch(`${API_BASE_URL}/${categories[category].endpoint}`, { signal })

  if (!response.ok) {
    throw new Error(`The archive returned an error (${response.status}).`)
  }

  const data: unknown = await response.json()
  if (!Array.isArray(data)) {
    throw new Error('The archive returned data in an unexpected format.')
  }

  return data as CatalogItem[]
}