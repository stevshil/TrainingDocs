# 10‑Minute Guided JavaScript Starter

This quick guide teaches you how to:

- Create an HTML page and attach a JavaScript file  
- Work with forms and user input  
- Send/receive JSON using REST APIs  
- Use `fetch`, `async`, `await`, and Promises  
- Build stylised popups  
- Store and display JSON data  

Each section includes:

- Explanation  
- Code to follow  
- Practice task  

---

## 1. Create Your First HTML + JavaScript Files (1 minute)

### What's happening

- A browser loads HTML first. When it reaches a `<script>` tag, it loads and runs the JavaScript file.  
- This separation keeps your code organised and easier to maintain.

### Follow this code

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
  <title>JS Starter</title>
  <!-- The next line includes the stylesheet into this file -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>My First JS App</h1>

  <!-- This line includes the JavaScript file into this file -->
  <script src="app.js"></script>
</body>
</html>
```

**app.js**
```javascript
// This line writes the text to the browser developer tools console.

console.log("JavaScript is connected!");
```

### Explanation

- `console.log()` prints to the browser's developer console.  
- If you see the message, your JS file is correctly linked.

> **NOTE 1:** to view this file it is best to use the **Go Live** button at the bottom right hand corner of VS Code.

> **NOTE 2:** You will need to open the developer tools in your web browser and have the **console** window open.  Refresh the screen if you do not see **JavaScript is connected** in the console.

> **NOTE 3:** When working with JavaScript it is best to use a development web server to view the pages, rather than loading just the file from disk.  Some JavaScript function will only work if they are provided through a web server.

### Practice

- Create a second JS file named **ui.js** and load it in the page.  
  - Have it print `"UI module loaded"`.
- Also add to the **alert** function to the file.  Alert functions will pop up a message box.
  - Have the alert show the text **"Danger Will Robinson"**
  - See https://developer.mozilla.org/en-US/docs/Web/API/Window/alert for details about the alert() function.

Refresh your browser, if you do not see the changes immediately in the console, or pop up on the screen.

> **NOTE:** The VS Code **Go Live** server normally refreshes when you save your work.

---

## 2. Build a Form to Collect User Input (1 minute)

### What's happening

- Forms let users enter data.  
- JavaScript listens for the form's **submit** event, stops the browser from reloading the page, and reads the input values.

### Follow this code

Add to **index.html**:

```html
<!-- Create a form for form elements -->
<form id="userForm">
  <!-- Create a text box to take a username -->
  <input type="text" id="username" placeholder="Enter username">
  <!-- Create a button to submit the form data -->
  <button type="submit">Send</button>
</form>
```

In **app.js**:

```javascript
// Waits for the form to be submitted
document.getElementById("userForm").addEventListener("submit", (e) => {
  e.preventDefault(); // stops page reload
  // Grabs the value typed in to the username field
  const name = document.getElementById("username").value;
  console.log("Name entered:", name);
});
```

### Explanation

- `addEventListener("submit")` runs code when the form is submitted.  
- `e.preventDefault()` stops the browser's default behaviour.  
- `.value` reads what the user typed.

### Practice

- Add a second field: **email**.  
- Log both values to the console window.
- Optional:
  - Add a third field **phone**

- Pushing yourself (very optional):
  - What about a selection of hobbies using a check list?
    - How do they appear in the console?
    - You might need a for loop, or be able to print an array to the console.

---

## 3. Send Form Data to a REST API (2 minutes)

### What's happening

- `fetch()` sends HTTP requests.  
- A POST request sends data to a server.  
- `JSON.stringify()` converts JS objects into JSON text.

### Follow this code

```javascript
async function sendData(name) {
  // Allows for a remote API call to be made.
  // We will discuss await/async shortly
  const response = await fetch("https://jsonplaceholder.typicode.com/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: name })
  });

  // Waits for the fetch to complete with the result.
  const data = await response.json(); // JSON → JS object
  console.log("API response:", data);
}

document.getElementById("userForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("username").value;
  // Calls our function to send the data to the API.  We don't use await here, even though the function is async, because it would pause the event handler causing further code to wait.
  // You would only await if you wanted to add a spinner, or disable the form until the request completed.
  sendData(name);
});
```

### Explanation

- `async` allows `await` inside the function.  
- `await fetch()` waits for the server to respond.  
  - POST defines the HTTP method to be used with the API
    - All APIs use GET/POST/PUT/DELETE and some make use of the other HTTP methods
    - Full list of methods https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
  - Content-Type is essential when working with APIs, as they generally expect JSON data if using POST/PUT or PATCH
- `response.json()` converts the JSON response into a usable JavaScript object.

### Practice

- Modify the body to send both **username** and **email**.
- Optional
  - Try calling the PUT method and updating one of the 2 values.

---

## 4. Create Stylised Popups Using HTML + CSS (2 minutes)

### What's happening

- A popup is just a `<div>` that is normally hidden.
- JavaScript toggles a CSS class to show or hide it.
- CSS makes it look like a modal window.

### Follow this code

Add to **index.html**:

```html
<!-- We're using the div container as a box -->
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

### Explanation

- `.popup` and `.popup-content` defines the box
- `.hidden` hides the popup.  
- `.classList.remove("hidden")` makes it visible.  
- You can display any message inside the popup.

### Practice

- Show the popup after a successful API POST.
- Optional:
  - See if you can toggle the pop up when clicking the button
  - This page should help https://developer.mozilla.org/en-US/docs/Web/API/Element/classList

---

## 5. Use `fetch`, `async`, `await`, and Promises (expanded to include Promise explanation)

### What's happening

JavaScript runs in a **single thread** - meaning it can only do one thing at a time.  But modern apps need to:

- load data from APIs  
- wait for servers  
- read files  
- perform long operations  

If JavaScript *waited* for each slow task, the browser would freeze.

### This is why Promises exist.

A **Promise** is an object that represents a value that will arrive *later*.  It's a placeholder for a future result.


Think of it like ordering food at a restaurant:

- You place the order → **Promise created**  
- You wait while the kitchen cooks → **Promise pending**  
- The waiter brings your food → **Promise resolved**  
- The kitchen burns your food → **Promise rejected**

JavaScript uses Promises to handle slow operations **without blocking the rest of the program**.

---

## Why we need Promises

### 1. They prevent the browser from freezing

JavaScript can continue running while waiting for network responses.

### 2. They allow clean handling of success and failure

A Promise can be:

- **resolved** → everything worked  
- **rejected** → something failed  

### 3. They are the foundation of `async` and `await`

`async` functions *always* return a Promise.  
`await` pauses execution until the Promise resolves.

---

## How Promises work with `fetch`

`fetch()` **always returns a Promise**.

```javascript
const promise = fetch("https://jsonplaceholder.typicode.com/users");
```

This Promise will eventually contain the server's response.

You can handle it with:

### Option A: `.then()`

```javascript
promise.then(response => {
  console.log("Got response:", response);
});
```

### Option B: `async` + `await`

You saw this being used earlier when POSTing data to an API.

```javascript
const response = await promise;
```

Both do the same thing - `await` is just cleaner.

---

## Follow this code

```javascript
async function loadUsers() {
  // Always wrap fetch in try, external exception
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    
    // JSON → JS object
    const users = await response.json();
    console.log("Loaded users:", users);
    
    // resolves the Promise
    return users;
  
  } catch (err) {
    console.error("Error loading users", err);
  }
}

// Using inline await (then) to wait for output.
// Call back in the brackets to capture the value returned by the promise.
loadUsers().then(users => {
  console.log("Promise resolved:", users);
});
```

---

## Explanation

- `fetch()` returns a **Promise** that will eventually contain the server response.  
- `await fetch()` pauses until the Promise resolves.  
- `response.json()` returns another Promise (because JSON parsing is async).  
- Returning `users` from the async function resolves the Promise returned by `loadUsers()`.  
- `.then()` receives the resolved value.

### Practice

- Add a `.catch()` to the Promise chain.

---

## 6. Store and Use JSON from REST APIs (2 minutes)

### What's happening

- You can store JSON data in a variable and use it later to update the page.  
- This is how single‑page apps work.

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

### Explanation

- `userCache` holds the JSON data.  
- `renderUsers()` builds HTML elements dynamically.  
- `forEach()` loops through the JSON array.

### Practice

Add a button that clears the list and reloads it.