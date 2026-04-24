import { createSlice, type PayloadAction } from "@reduxjs/toolkit";
import { type Person } from "../types/Person";

interface PeopleState {
  list: Person[];
}

const initialState: PeopleState = {
  list: [
    {
      name: "Alice Johnson",
      age: 32,
      hobbies: ["Reading", "Running"],
      favouriteColour: "Blue",
    },
    {
      name: "Michael Smith",
      age: 41,
      hobbies: ["Golf", "Cooking"],
      favouriteColour: "Green",
    },
  ],
};

interface UpdatePayload {
  originalName: string;
  updated: Person;
}

const peopleSlice = createSlice({
  name: "people",
  initialState,
  reducers: {
    addPerson: (state, action: PayloadAction<Person>) => {
      state.list.push(action.payload);
    },
    updatePerson: (state, action: PayloadAction<UpdatePayload>) => {
      const index = state.list.findIndex(
        (p) => p.name === action.payload.originalName
      );
      if (index !== -1) state.list[index] = action.payload.updated;
    },
    deletePerson: (state, action: PayloadAction<string>) => {
      state.list = state.list.filter((p) => p.name !== action.payload);
    },
  },
});

export const { addPerson, updatePerson, deletePerson } = peopleSlice.actions;
export default peopleSlice.reducer;
