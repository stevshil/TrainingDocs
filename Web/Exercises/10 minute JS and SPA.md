# 10‑Minute JavaScript Starter Course (Full Integrated Guide)

This course teaches you how to:

- Create an HTML page and attach a JavaScript file  
- Work with forms and user input  
- Send/receive JSON using REST APIs  
- Use `fetch`, `async`, `await`, and Promises  
- Build stylised popups  
- Store and display JSON data  
- Build a simple Single Page Application (SPA)  

Each section includes:

- Explanation
- Code to follow
- Practice task

No fluff. No frameworks. Just clean, modern JavaScript.

---

# 1. Create Your First HTML + JavaScript Files (1 minute)

### What's happening

The browser loads HTML first. When it reaches a `<script>` tag, it loads and runs your JavaScript file.

### Follow this code

**index.html**

```html
<!DOCTYPE html>
<html>
<head>
  <title>JS Starter</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>My First JS App</h1>

  <script src="app.js"></script>
</body>
</html>
```

**app.js**

```javascript
console.log("JavaScript is connected!");
```

### Practice

Create a second JS file named **ui.js** and load it in the page.  
Have it print `"UI module loaded"`.

---

# 2. Build a Form to Collect User Input (1 minute)

### What's happening

Forms let users enter data. JavaScript listens for the form's **submit** event and reads the input values.

### Follow this code

Add to **index.html**:

```html
<form id="userForm">
  <input type="text" id="username" placeholder="Enter username">
  <button type="submit">Send</button>
</form>
```

In **app.js**:

```javascript
document.getElementById("userForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("username").value;
  console.log("Name entered:", name);
});
```

### Practice

Add a second field: **email**. Log both values.

---

# 3. Send Form Data to a REST API (2 minutes)

### What's happening

`fetch()` sends HTTP requests.  
A POST request sends data to a server.  
`JSON.stringify()` converts JS objects into JSON text.

### Follow this code

```javascript
async function sendData(name) {
  const response = await fetch("https://jsonplaceholder.typicode.com/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: name })
  });

  const data = await response.json();
  console.log("API response:", data);
}
```

### Practice

Modify the body to send both **username** and **email**.

---

# 4. Create Stylised Popups Using HTML + CSS (2 minutes)**

### What's happening**
A popup is just a `<div>` that is normally hidden.  
JavaScript toggles a CSS class to show or hide it.

### Follow this code**

Add to **index.html**:

```html
<div id="popup" class="hidden">
  <div class="popup-content">
    <p id="popupMessage"></p>
    <button id="closePopup">Close</button>
  </div>
</div>
```

**styles.css**

```css
#popup {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.6);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
}

.hidden {
  display: none;
}
```

**app.js**
```javascript
function showPopup(message) {
  document.getElementById("popupMessage").textContent = message;
  document.getElementById("popup").classList.remove("hidden");
}

document.getElementById("closePopup").addEventListener("click", () => {
  document.getElementById("popup").classList.add("hidden");
});
```

### Practice

Show the popup after a successful API POST.

---

# 5. Use `fetch`, `async`, `await`, and Promises (expanded)

### Why Promises exist

JavaScript is single‑threaded.  
If it waited for slow operations (network, files), the browser would freeze.

A **Promise** is a placeholder for a value that arrives later.

### Promise lifecycle**
- **Pending** → waiting  
- **Resolved** → success  
- **Rejected** → failure  

### Why we need Promises**
- They prevent blocking  
- They handle success/failure cleanly  
- They are the foundation of `async`/`await`

### Follow this code

```javascript
async function loadUsers() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const users = await response.json();
    console.log("Loaded users:", users);
    return users;
  } catch (err) {
    console.error("Error loading users", err);
  }
}

loadUsers().then(users => {
  console.log("Promise resolved:", users);
});
```

### Practice

Add a `.catch()` to the Promise chain.

---

# 6. Store and Use JSON from REST APIs (2 minutes)

### What's happening

You can store JSON data in a variable and use it later to update the page.

### Follow this code

```javascript
let userCache = [];

async function loadAndStore() {
  const response = await fetch("https://jsonplaceholder.typicode.com/users");
  userCache = await response.json();
  renderUsers();
}

function renderUsers() {
  const list = document.createElement("ul");
  userCache.forEach(u => {
    const li = document.createElement("li");
    li.textContent = `${u.name} (${u.email})`;
    list.appendChild(li);
  });
  document.body.appendChild(list);
}

loadAndStore();
```

### Practice

Add a button that clears the list and reloads it.

---

# 7. Build a Simple Single Page Application (SPA) (3 minutes)

### What's happening

A SPA loads **one HTML file** and uses JavaScript to swap content dynamically.  
Navigation happens through **hash‑based routing** (e.g., `#/about`).

---

## 7.1 HTML Shell

Add this to **index.html**:

```html
<nav>
  <a href="#/">Home</a>
  <a href="#/about">About</a>
  <a href="#/contact">Contact</a>
</nav>

<div id="app"></div>
```

---

## 7.2 Page Functions

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

---

## 7.3 Router

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

---

## 7.4 Add Dynamic State (Counter Page)

```javascript
let count = 0;

function counterPage() {
  return `
    <h1>Counter</h1>
    <p>Count: ${count}</p>
    <button id="incBtn">Increment</button>
  `;
}

routes['#/counter'] = counterPage;
```

Add event listener:

```javascript
if (hash === '#/counter') {
  document.getElementById('incBtn').addEventListener('click', () => {
    count++;
    router();
  });
}
```

---

## SPA Practice

- Add a new page called **Services**  
- Add a new navigation link  
- Display a list of services using `<ul>`  