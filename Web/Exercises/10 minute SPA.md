# Build a Simple Single Page Application (SPA) with HTML, CSS & JavaScript

## Takeaway

A Single Page Application loads **one HTML file** and uses JavaScript to **swap content dynamically** when the user navigates. No page reloads. No frameworks. Just clean, modern JavaScript.

---

# 1. What a SPA Is (and Why It Matters)

A **Single Page Application (SPA)**:

- Loads **one HTML page**  
- Uses **client‑side routing** (e.g., URL hashes like `#/about`)  
- Dynamically injects content into a container  
- Feels fast because it avoids full page reloads  

This matches the core definition of SPAs: a single HTML file with dynamic content updates and hash‑based routing   [DEV Community](https://dev.to/moseeh_52/building-modern-spas-with-vanilla-javascript-a-beginners-guide-9a3).

---

# 2. Project Structure

Create a folder:

```
simple-spa/
  index.html
  styles.css
  app.js
```

---

# 3. Build the HTML Shell

This HTML file never reloads. All "pages" are injected into the `#app` container.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Simple SPA</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <nav>
    <a href="#/">Home</a>
    <a href="#/about">About</a>
    <a href="#/contact">Contact</a>
  </nav>

  <div id="app"></div>

  <script src="app.js"></script>
</body>
</html>
```

### Explanation

- The `<nav>` links update the URL hash (e.g., `#/about`).  
- The `<div id="app">` is where JavaScript injects page content.  
- This structure matches common SPA patterns: navigation + dynamic content container   [DEV Community](https://dev.to/moseeh_52/building-modern-spas-with-vanilla-javascript-a-beginners-guide-9a3).

---

# 4. Add Basic Styling

```css
body {
  font-family: Arial, sans-serif;
  margin: 20px;
}

nav a {
  margin-right: 20px;
  text-decoration: none;
  font-weight: bold;
}

#app {
  margin-top: 20px;
}
```

---

# 5. Create Page Content Functions

Each function returns HTML for a "page."

```javascript
function homePage() {
  return `
    <h1>Home</h1>
    <p>Welcome to our simple SPA!</p>
  `;
}

function aboutPage() {
  return `
    <h1>About</h1>
    <p>This SPA was built with plain JavaScript.</p>
  `;
}

function contactPage() {
  return `
    <h1>Contact</h1>
    <p>Email us at example@example.com</p>
  `;
}
```

### Explanation

This mirrors the pattern of returning HTML strings for each route, as shown in modern vanilla‑JS SPA tutorials   [DEV Community](https://dev.to/moseeh_52/building-modern-spas-with-vanilla-javascript-a-beginners-guide-9a3).

---

# 6. Build a Simple Router

```javascript
const routes = {
  '#/': homePage,
  '#/about': aboutPage,
  '#/contact': contactPage
};

function router() {
  const hash = window.location.hash || '#/';
  const page = routes[hash];

  document.getElementById('app').innerHTML =
    page ? page() : `<h1>404 - Page Not Found</h1>`;
}

window.addEventListener('hashchange', router);
window.addEventListener('load', router);
```

### Explanation

- Hash‑based routing is the simplest SPA routing method and works without a server.  
- When the hash changes, the router loads the correct page.  
- This approach is consistent with SPA routing patterns described in vanilla‑JS guides   [DEV Community](https://dev.to/moseeh_52/building-modern-spas-with-vanilla-javascript-a-beginners-guide-9a3).

---

# 7. Add Dynamic Content (Optional Enhancement)

Let’s add a "counter page" to show dynamic state — a common SPA teaching example   [javaspring.net](https://www.javaspring.net/blog/single-page-application-implemented-with-javascript-jquery/).

### Add a new page

```javascript
let count = 0;

function counterPage() {
  return `
    <h1>Counter</h1>
    <p>Count: ${count}</p>
    <button id="incBtn">Increment</button>
  `;
}
```

### Add route

```javascript
routes['#/counter'] = counterPage;
```

### Add event listener after rendering

```javascript
function router() {
  const hash = window.location.hash || '#/';
  const page = routes[hash];

  document.getElementById('app').innerHTML =
    page ? page() : `<h1>404 - Page Not Found</h1>`;

  if (hash === '#/counter') {
    document.getElementById('incBtn').addEventListener('click', () => {
      count++;
      router(); // re-render
    });
  }
}
```

### Explanation

- This demonstrates SPA state management: the counter value persists across renders.  
- Re-rendering the page after updating state is a core SPA concept.

---

# 8. Practice Tasks

### Beginner Tasks

- Add a new page called **Services**.  
- Add a new navigation link.  
- Display a list of services using `<ul>`.

### Intermediate Tasks

- Add a form to the Contact page.  
- Capture input and display it dynamically.  
- Add a "loading spinner" that appears before content loads.

### Advanced Tasks

- Fetch data from a REST API and display it inside a page.  
- Add error handling and a retry button.  
- Add a popup (from your earlier course) when data loads successfully.

---

# 9. Summary

You now have a working SPA with:

- Hash‑based routing  
- Dynamic content injection  
- Multiple pages  
- State management  
- Expandable architecture  

This matches the core SPA principles described in modern vanilla‑JS tutorials: single HTML file, client‑side routing, and dynamic content updates   [DEV Community](https://dev.to/moseeh_52/building-modern-spas-with-vanilla-javascript-a-beginners-guide-9a3).