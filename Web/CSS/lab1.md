# CSS Styling

This lab uses [HTML lab1](../HTML/lab1.md) as the starting lab.

# CSS Enhancement

**Goal:** Improve the look, layout, and usability of your existing pages using modern CSS techniques.

This add‑on must be completed **after** finishing Option 1, 2, or 3.

---

## Part 1 — Replace Any Non‑Data Tables With CSS Layout

If your chosen option uses a table **only for layout**, you must:

* Remove the layout table  
* Rebuild the layout using **Flexbox**  
* Keep real data tables (e.g., hobby lists, availability tables, comparison tables)

**Examples of acceptable replacements:**

* A 3‑column section → Flexbox  
* A navigation bar → Flexbox  
* A card layout → Flexbox  

---

## Part 2 — Add a Flexbox Layout Section

Add at least **one new section** to any page that uses Flexbox.

Examples:

* A row of "cards" (each with an image + text)  
* A horizontal navigation bar  
* A responsive gallery  
* A two‑column layout (text + image)

**Requirements:**

* Use `display: flex`  
* Add spacing using `gap`, `padding`, or `margin`  
* Use `justify-content` and/or `align-items`  

---

## Part 3 — Style Your Buttons and Links

All buttons and important links must be styled using CSS.

**Required features:**

* Custom background colour  
* Rounded corners  
* Hover effect (colour change, scale, underline, etc.)  
* Padding for better clickability  

**Example:**

```css
button {
  background: #4a90e2;
  color: white;
  padding: 10px 18px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background: #357ab8;
  transform: scale(1.05);
}
```

---

## Part 4 — Improve Form UI

You must style **all forms** in your project.

Look at some web sites to get ideas, or use the references at the bottom of this document.

**Requirements:**

* Add spacing between form fields  
* Style `<input>`, `<select>`, and `<textarea>`  
* Add focus styles (e.g., glowing border)  
* Style the submit button (see Part 3)

**Example:**
```css
input, select, textarea {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

input:focus, textarea:focus {
  border-color: #4a90e2;
  outline: none;
}
```

---

## Part 5 — Add a Styled "Card" Component

Add at least **one** card somewhere in your site.

A card must include:

* A container `<div>`  
* An image  
* A heading  
* A paragraph  
* A link or button  

**CSS Requirements:**

* Border or shadow  
* Padding  
* Rounded corners  
* Hover effect (shadow or scale)

---

## Part 6 — Add a Global Style Sheet

Create a `styles.css` file and link it to **all pages**.

Your stylesheet must include:

* A colour palette (at least 3 colours)  
* A consistent font (Google Fonts allowed)  
* Styled headings  
* Styled paragraphs  
* A consistent layout spacing system (e.g., `margin-bottom: 1rem;`)  

---

## Bonus (Optional)

Add **basic responsiveness**:

* Flexbox wrapping  
* A mobile‑friendly nav bar  
* Images that scale with the screen

## Useful references

* [The Largest Library of Open-Source UI](https://uiverse.io/)
* [Try out your HTML/CSS before](https://codepen.io/brundolf/pen/gRaREv)
* [A useful grid layout and online designing tool](https://jsfiddle.net/)
* [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [CSS Tricks](https://css-tricks.com/)
* [CSS Zen Garden - awesome ideas CSS no JavaScript](https://csszengarden.com/)