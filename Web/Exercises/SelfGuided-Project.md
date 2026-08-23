# Responsive Single‑Page Web Application Using HTML, CSS & JavaScript (No Frameworks)

### *3‑Hour Progressive Learning Project*

The project is aimed at all levels, so you can technically start in different locations, but you will need to read through the steps to make sure you have built the necessary parts for the end, and have the relevant interactions within the page.

The aim is to allow you to work at your speed, and if a group of you are stuck in a similar area ask for a breakout learning session.

---

# 1. Project Overview

In this project, you will build a responsive web front end that evolves from:

### Static HTML → Styled multi-page site → Interactive JavaScript → Dynamic table → Single‑Page Application → API-powered CRUD app

The project supports **all skill levels**:

- **Beginners** follow guided steps to learn HTML, CSS, and JavaScript fundamentals.
- **Intermediate** use tutorials and references to build a full SPA with CRUD operations.
- **Advanced** can add optional enhancements.

You will learn:

- HTML structure, forms, tables, navigation  
- CSS layout, responsive design, styling  
- JavaScript DOM manipulation  
- Event handling  
- Sorting, filtering, dynamic table generation  
- Fetch API, Promises, async/await  
- CRUD operations with a real API  
- SPA architecture without frameworks  

## Before starting

- Create a new directory in your favourite coding location on your computer.
- Call the directory **LearningWeb**
- Open this directory in **VS Code**
- Now you are ready

---

# 2. Free APIs You Can Use Later

Choose **one** API when you reach the API stage.

### Full CRUD APIs (GET/POST/PUT/DELETE/PATCH)

- JSONPlaceholder - https://jsonplaceholder.typicode.com 
- DummyJSON - [https://dummyjson.com](https://dummyjson.com)  
- ReqRes - [https://reqres.in](https://reqres.in)  

### Fun APIs (GET only - beginner friendly)

- PokéAPI - [https://pokeapi.co](https://pokeapi.co)  
- The Cat API - [https://thecatapi.com](https://thecatapi.com)  
- The Dog API - [https://thedogapi.com](https://thedogapi.com)  
- Studio Ghibli API - [https://ghibliapi.vercel.app](https://ghibliapi.vercel.app)  

### Weather & Location APIs

- Open-Meteo - [https://open-meteo.com](https://open-meteo.com)  
- OpenStreetMap Nominatim - [https://nominatim.openstreetmap.org](https://nominatim.openstreetmap.org)  

### API Directory

- Public APIs Directory - https://github.com/public-apis/public-apis

> **NOTE:** You are free to use any API you wish to for your project, but you must be able to perform the necessary elements of the project.

---

# 3. Beginner Section - Guided Learning

Beginners follow these steps in order.  
Intermediate learners may skip ahead.

---

# Step 1 - Create Your Multi-Page HTML Website

Create the following pages:

- `index.html` - Home  
- `list.html` - Shows your table  
- `detail.html` - Shows details of one item  
- `create.html` - Form to add new data  

This are just text files, but ensure that you create them in your VS Code area for this project.

### Required HTML elements

- `<header>`, `<nav>`, `<main>`, `<footer>`  
- `<form>` with:  
  - `<input type="text">`  
  - `<textarea>`  
  - `<select>`  
  - `<button>`  
- `<table>`  
- `<a>` links for navigation

### Beginner Tutorials

- HTML basics - https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
- HTML forms - https://developer.mozilla.org/en-US/docs/Learn/Forms
- HTML tables - https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables

---

# Step 2 - Add Static Example Data to Your Table

Choose **one** dataset below and manually create your own HTML table in `list.html`.

### Dataset A - "Posts"

| ID | Title | Author | Summary |
|----|-------|--------|---------|
| 1 | Welcome to My Blog | Alice | Intro to the blog. |
| 2 | Learning HTML | Bob | Basic HTML tags. |
| 3 | CSS Tips | Charlie | Improve your layout. |
| 4 | JavaScript Basics | Dana | Variables & functions. |
| 5 | Working With APIs | Erin | Fetching data. |

### Dataset B - "Animals"

| ID | Name | Type | Description |
|----|------|------|-------------|
| 101 | Luna | Cat | Playful climber. |
| 102 | Max | Dog | Energetic walker. |
| 103 | Bella | Cat | Quiet & affectionate. |
| 104 | Rocky | Dog | Loves fetch. |
| 105 | Milo | Cat | Curious explorer. |

### Dataset C - "Characters"

| ID | Name | Origin | Power Level |
|----|------|--------|-------------|
| 201 | Totoro | Forest Spirit | 95 |
| 202 | Pikachu | Kanto Region | 88 |
| 203 | Kiki | Koriko | 72 |
| 204 | Jiji | Koriko | 60 |
| 205 | Charmander | Kanto Region | 85 |

You must write the HTML table yourself.

---

# Step 3 - Add CSS Styling & Responsive Layout

Create a new file called `styles.css` and link it to all the HTML pages.

> Use web search or Copilot to find out how to link an external resource file like a stylesheet in an HTML file.

### Required CSS concepts

- Flexbox  
- Grid  
- Media queries  
- Styling tables  
- Styling buttons  
- Colour palette & typography

### Beginner Tutorials

- CSS layouts - https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout
- Responsive design - https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design
- CSS styling basics - https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps

### Useful online tools

- Screen layouts using stylesheets
  - https://talos.tools/grid
  - https://onedev.tools/css-layout
  - https://99tools.net/css-layout-generator/
  - https://talos.tools/grid

### Awesome CSS ideas

Some awesome ideas to whet your appetite.

- https://awesome-css.com
- https://csszengarden.com
  - No JavaScript, just CSS - https://csszengarden.com/219/

### Tasks
1. Style the header and navigation using Flexbox.
    - Choose a style that you like in positioning your navigation.
    - Where would navigation be best for your users or page.
2. Style the table (borders, alternating row colours, hover effects).
    - Consider shadows, gradients, colour, etc
3. Style form elements (inputs, selects, buttons).
    - Do you want your buttons or boxes to look 3D?
    - Font sizes and colouring, etc.
4. Add media queries for mobile/tablet/desktop.
    - These are CSS that have the `@media` directive and affect the way the screen shows on different devices.
    - Use Copilot or web search to find code that meets the devices you want to work with.

---

# Step 4 - First JavaScript: Pop-Up Messages & Button Interactions

Before working with data, learn basic JavaScript interactions.

### Beginner Tutorials

- JavaScript basics - https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
- DOM manipulation - https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction
- Online interactive JavaScript tutorial - https://www.ubyte.dev/tutorial/javascript

### Tasks

1. Create `app.js` and link it to **index.html**.  
2. Add a button that shows a styled pop-up message (a `<div>` that appears).  
3. Add a click event to each table row that shows a pop-up with the row’s details.  
4. Add a button that changes the page’s theme (light/dark).

> **NOTE:** If the single file gets too complex, you can split your JavaScript across files.  Think of it like creating different Java classes, but you'll need to ensure that you don't split items that are related.

This builds confidence before touching dynamic data.

---

# Step 5 - Add JavaScript-Controlled Table Features (Still Static Data)

Now convert your static table into a dynamic JavaScript-generated table.

### Tasks

1. Create a JavaScript array of objects that matches your dataset.  
2. Write a loop that builds the table rows dynamically.  
3. Add a `<select>` box that changes how many rows are shown (e.g., 3, 5, 10).  
4. Add click events to table headings to sort the data.  
5. Add a filter box to search by name/title.

### Tutorials

- JavaScript arrays - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- Loops - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration
- Events - https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener

You now have a fully interactive table **without using any API yet**.

---

# Step 6 - Fetch API: Load Real Data (GET Only)

Now replace your static JavaScript array with real API data.

### Tutorials

- Fetch API - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetchorg%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetch_API%2FUsing_Fetch
- Async/await - https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await

### Tasks

1. Choose an API from the list.  
2. Write a function that fetches data using `fetch()`.  
3. Replace your static array with the API data.  
4. Reuse your dynamic table code to display the API data.  
5. Add error handling and loading messages.

Beginners finish here.

---

# 7. Intermediate Section - Self-Directed Development

Intermediate level now build a full SPA with CRUD operations.

### Tutorials

- Build a simple SPA - https://www.freecodecamp.org/news/build-a-single-page-app-without-frameworks/  
- JavaScript modules - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules  
- State management basics - https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
- Client-side routing - https://developer.mozilla.org/en-US/docs/Web/API/History_API 
- LocalStorage - https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage

### Required Features

1. **List View**  
2. **Detail View**  
3. **Create View (POST)**  
4. **Edit View (PUT/PATCH)**  
5. **Delete Functionality**  
6. **SPA Navigation (hash-based)**  

---

# 8. Optional Advanced Enhancements

- LocalStorage caching  
- Optimistic UI updates  
- Pagination or infinite scroll  
- Image uploads  
- Custom events  
- Theme switcher  
- Animations  

---

# 9. Final Deliverables

### Beginners

- Multi-page HTML site  
- Styled responsive layout  
- Pop-up interactions  
- Dynamic table (sorting, filtering, select box)  
- API-powered GET requests  

### Intermediate

- Fully functional SPA  
- CRUD operations  
- Modular JavaScript  
- Error handling  
- Responsive UI  

### Advanced

- Optional enhancements
- Routing  
- State management  
- UI components