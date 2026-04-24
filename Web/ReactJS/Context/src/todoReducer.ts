import type { Todo } from "./Todo";

export type TodoAction =
  | { type: "toggle"; id: number }
  | { type: "add"; text: string };

export function todoReducer(state: Todo[], action: TodoAction): Todo[] {
  switch (action.type) {
    case "toggle":
      return state.map(todo =>
        todo.id === action.id
          ? { ...todo, completed: !todo.completed }
          : todo
      );
    case "add": {
      const maxId = state.length > 0
        ? Math.max(...state.map(t => t.id))
        : 0;

      return [
        ...state,
        {
          id: maxId + 1,
          text: action.text,
          completed: false
        }
      ];
    };
    case "adds": {
      // Step 1: Create a variable to hold the new ID
      let newId = 0;

      // Step 2: Check if the state array has any todos
      if (state.length > 0) {
        // Step 3: Create an array containing only the IDs
        const idList = state.map(function (todo) {
          return todo.id;
        });

        // Step 4: Find the maximum ID in the list
        const maxId = Math.max.apply(null, idList);

        // Step 5: Increment the maximum ID to get the new ID
        newId = maxId + 1;
      } else {
        // Step 6: If there are no todos, start IDs at 1
        newId = 1;
      }

      // Step 7: Create a new todo object
      const newTodo = {
        id: newId,
        text: action.text,
        completed: false
      };

      // Step 8: Create a new array that includes all existing todos plus the new one
      const updatedList = state.concat(newTodo);

      // Step 9: Return the updated array
      return updatedList;
    };
    default:
      return state;
  }
}