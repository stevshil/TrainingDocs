export type Category = 'characters' | 'planets' | 'starships'

export interface Character {
  name: string
  height: string
  mass: string
  hair_color: string
  skin_color: string
  eye_color: string
  birth_year: string
  gender: string
  homeworld: string
  films: string[]
  species: string[]
  vehicles: string[]
  starships: string[]
  url: string
}

export interface Planet {
  name: string
  rotation_period: string
  orbital_period: string
  diameter: string
  climate: string
  gravity: string
  terrain: string
  surface_water: string
  population: string
  residents: string[]
  films: string[]
  url: string
}

export interface Starship {
  name: string
  model: string
  manufacturer: string
  cost_in_credits: string
  length: string
  max_atmosphering_speed: string
  crew: string
  passengers: string
  cargo_capacity: string
  consumables: string
  hyperdrive_rating: string
  MGLT: string
  starship_class: string
  pilots: string[]
  films: string[]
  url: string
}

export type CatalogItem = Character | Planet | Starship

export interface CategoryConfig {
  label: string
  singular: string
  endpoint: string
  description: string
  accent: string
}

export const categories: Record<Category, CategoryConfig> = {
  characters: {
    label: 'Characters',
    singular: 'character',
    endpoint: 'people',
    description: 'People who shaped the course of galactic history.',
    accent: 'copper',
  },
  planets: {
    label: 'Planets',
    singular: 'planet',
    endpoint: 'planets',
    description: 'Worlds, moons, and the civilizations built upon them.',
    accent: 'mint',
  },
  starships: {
    label: 'Starships',
    singular: 'starship',
    endpoint: 'starships',
    description: 'Vessels that cross the distance between the stars.',
    accent: 'blue',
  },
}

export const isCategory = (value: string | undefined): value is Category =>
  value !== undefined && value in categories