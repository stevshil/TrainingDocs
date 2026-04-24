import CounterWatcher from "./CounterWatcher";
import UserComponent from "./UserComponent";
import WindowWidth from "./WindowWidth";
import Timer from "./Timer";
import FocusInput from "./FocusInput";
import ClickCounter from "./ClickCounter";
import PreviousValue from "./PreviousValue";
import { useTheme } from "./ThemeProvider";

function App() {
  const { theme, toggleTheme } = useTheme();
  return (
    <>
    <div>
      <UserComponent />
      <CounterWatcher />
      <WindowWidth />
      <Timer />
      <FocusInput />
      <ClickCounter />
      <PreviousValue />
    </div>
    <div
      style={{
        background: theme === "light" ? "#fff" : "#222",
        color: theme === "light" ? "#000" : "#fff",
        height: "100vh",
        padding: "2rem",
      }}
    >
      <h1>Current theme: {theme}</h1>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
    </>
  );
}

export default App;
