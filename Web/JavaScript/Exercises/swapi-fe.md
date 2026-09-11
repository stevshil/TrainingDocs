# **TS + SWAPI Lab — Handout**

### *Building a Responsive Web Frontend Using TypeScript, Fetch API, CSS Grid, and External APIs*

You may use Copilot to help build the app, but you need to work out the interactions that the user would require.

If you've been working with Gen AI and have an app that supplies data, see if you can link your frontend with that.
- Python Flask for FastAPI can help generate API services

---

## **1. Lab Overview**
In this lab you will build a **fully responsive web application** using:

- **TypeScript → JavaScript** (compiled with `npx tsc` or run with `npx tsx`)
- **Raw DOM manipulation** (no frameworks)
- **Fetch API** for HTTP requests
- **SWAPI (Star Wars API)** for GET requests  
- **Optional: DummyJSON API** for POST, PUT, DELETE
- **CSS Grid + Flexbox** for layout
- **Responsive design** for **mobile, tablet, and desktop**
- **Local images** for characters or items

You will create the project **from a specification**, with only minimal code snippets provided.  
This lab assumes you have already completed a basic coding exercise.

---

## **2. Learning Objectives**
By the end of this lab, you will be able to:

- Build a TypeScript‑driven web frontend without frameworks  
- Use Fetch API with async/await  
- Render API data dynamically into the DOM  
- Create responsive layouts using CSS Grid and media queries  
- Structure a project using TypeScript modules  
- Integrate external APIs (GET required, CRUD optional)  
- Convert a multi‑page site into a single‑page application (SPA)

---

## **3. Project Requirements**
You must create the following:

### **Required**
- A **multi‑page website** (later converted to SPA)
- A **responsive layout** supporting:
  - Mobile (≤600px)
  - Tablet (601–900px)
  - Desktop (≥901px)
- A **CSS Grid‑based table/card layout**
- A **banner image** and **per‑item images**
- TypeScript code compiled to JavaScript
- Fetching and displaying SWAPI data:
  - People
  - Planets
  - Starships

### **Optional (Advanced)**
Use DummyJSON API to implement:
- POST (add)
- PUT (update)
- DELETE (remove)

---

## **4. APIs You Will Use**

### **Primary API — SWAPI (GET only)**
Example endpoints:
- People: [https://swapi.dev/api/people/](https://swapi.dev/api/people/)
- Planets: [https://swapi.dev/api/planets/](https://swapi.dev/api/planets/)
- Starships: [https://swapi.dev/api/starships/](https://swapi.dev/api/starships/)

You must:
- Fetch lists
- Display selected details
- Provide your own images (e.g., `/assets/luke.png`)

### **Optional CRUD API — DummyJSON**
- GET: [https://dummyjson.com/products](https://dummyjson.com/products)  
- POST: [https://dummyjson.com/products/add](https://dummyjson.com/products/add)  
- PUT: [https://dummyjson.com/products/1](https://dummyjson.com/products/1)  
- DELETE: [https://dummyjson.com/products/1](https://dummyjson.com/products/1)  

---

## **5. Project Structure**
You must create this structure manually:

```
ts-swapi-lab/
│
├── index.html
├── styles.css
│
├── src/
│   └── main.ts
│
├── dist/
│   └── main.js   (compiled output)
│
└── assets/
    └── images...
```

---

## **6. Minimum Code Snippets Provided**
You may use these snippets, but you must expand them.

### **Fetch Example**
```ts
async function loadPeople() {
  const response = await fetch("https://swapi.dev/api/people/");
  const data = await response.json();
  return data.results;
}
```

### **CSS Grid Example**
```css
.grid-table {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}
```

### **Media Query Example**
```css
@media (max-width: 600px) {
  .grid-table {
    grid-template-columns: 1fr;
  }
}
```

---

## **7. Stage Breakdown**

### **Stage 1 — Multi‑Page HTML**
Create:
- `index.html` (home + banner image)
- `people.html` (button + results area)
- `about.html` (static content + image)

### **Stage 2 — CSS Styling**
Implement:
- CSS Grid for tables/cards  
- Flexbox for navigation  
- Media queries for responsiveness  
- Scalable images  

### **Stage 3 — TypeScript Fetch**
Render SWAPI data into:
- Cards  
- Grid tables  
- Sections with images  

### **Stage 4 — Convert to SPA**
Replace multiple pages with:
- One `index.html`
- Navigation buttons
- Hidden/visible sections
- Dynamic rendering

### **Stage 5 — Optional CRUD**
Use DummyJSON to:
- Add items  
- Update items  
- Delete items  
- Display results in responsive grid format  

---

## **8. What You Must Submit**
Your final submission must include:

- Git repository URL that I can access
- Working responsive website  
- TypeScript source code  
- Compiled JavaScript  
- Images used in the project  
- A short README explaining:
  - How to run the project  
  - Which APIs you used  
  - Which optional features you completed  

---

## **9. Marking Criteria**

### **Beginner Level**
- Multi‑page HTML  
- Responsive CSS Grid  
- SWAPI GET requests  
- Images included  
- Basic DOM manipulation  

### **Intermediate Level**
- SPA conversion  
- Multiple SWAPI endpoints  
- Dynamic rendering  
- Form inputs  

### **Advanced Level**
- CRUD operations  
- Error handling  
- Loading indicators  
- Modular TypeScript  

---

## **10. Tips for Success**
- Build the layout first, then add TypeScript logic.  
- Test API calls in the browser console before coding.  
- Keep your grid flexible—avoid fixed widths.  
- Use `console.log()` heavily during development.  
- Commit regularly and keep your code modular.