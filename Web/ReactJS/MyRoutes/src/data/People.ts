import {searchPeople, type Person} from '../types/Person';

// Create a list of people
export const people: Person[] = [
  { name: "Alice", age: 28, hobby: "Painting" },
  { name: "Ben", age: 34, hobby: "Cycling" },
  { name: "Chloe", age: 22, hobby: "Gaming" },
  { name: "David", age: 41, hobby: "Cooking" },
  { name: "Steve", age: 21, hobby: "Fast cars" }
];

export default searchPeople;