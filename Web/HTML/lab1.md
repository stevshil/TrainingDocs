# HTML Lab options

During this exercise you should make sure you cover the following essential tags;

**Document Structure**
```
<!DOCTYPE html>
<html>
<head>
<title>
<body>
<header>, <main>, <footer>
```

**Text Formatting**
```
<h1> to <h6>
<p>
<strong>, <em>
<br>
<span>, <div>
```

**Lists**
```
<ul>, <ol>, <li>
```

**Links & Media**
```
<a>
<img>
```

**Tables**
<table>
<thead>, <tbody>
<tr>, <th>, <td>
```

**Forms**
```
<form>
<label>
<input> (text, email, number, radio, checkbox)
<textarea>
<select>, <option>
<button> or <input type="submit">
```

---

## Option 1 - **My Personal Mini‑Website**

**Goal:** Create a simple 3‑page personal website about yourself, your hobbies, and your favourite things.

Pages to Create;

1. index.html - **About Me**
    * Introduce yourself
    * Add a photo (real or avatar)
    * Include a list of interests
    * Add links to the other two pages
    * Use nested tags (e.g., \<p\>\<strong\>text\</strong\>\</p\>)
    * Form **Send me a message** containing the fields;
      * name
      * Email address
      * favourite hobby selection list
      * message text area
      * submit button
2. hobbies.html - **My Hobbies**
    * Create a table listing at least 3 hobbies
        * Columns: Hobby, How long you've done it, Why you enjoy it, links to pages explaining your hobby
    * Add images related to each hobby
    * Add a link back to index.html and to favourites.html
3. favourites.html - **My Favourite Things**
    * Add links to favourite websites (games, sports teams, books, music, etc.)
    * Include at least one ordered list and one unordered list
    * Add nested tags (e.g., \<em\>\<a href="..."\>Favourite link\</a\>\</em\>)
    * Link back to the other pages

Required HTML Features;

* \<a\> links between pages
* \<img\> images
* \<table\> with \<thead\>, \<tbody\>, \<tr\>, \<td\>
* Nested tags (e.g., \<p\>\<strong\>bold text\</strong\>\</p\>)
* Lists (\<ul\>, \<ol\>)

---

## Option 2 - **The Three‑Page Portfolio**

**Goal:** Build a simple CV or portfolio of yourself, e.g. a LinkedIn profile, but better.

Pages to Create;

1. home.html - **Welcome**
    * Intro paragraph
    * Image or avatar or you
    * A nested structure like:
      html
      \<div\>
        \<p\>Hi, I'm \<strong\>...\</strong\>\</p\>
      \</div\>
    * A small table showing **Skills I'm Learning**
    * Links to projects.html and contact.html
    * Form **join my mailing list** with the following fields;
      * Name
      * Email address
      * Dropdown menu **what you are interested in**
      * Text area for message
      * Submit button
2. projects.html - **My Projects**
    * Describe 2-3 imaginary or real projects
    * Include images (screenshots or placeholders)
    * Add links to external resources (GitHub, tutorials, etc.)
    * Link back to home.html and contact.html
3. contact.html - **Contact Me**
    * A fake contact section
    * A table showing availability (e.g., days of the week)
    * A list of ways to reach them (email, LinkedIn, etc.)
    * Link back to the other pages

Required HTML Features;

* Semantic structure encouraged (\<header\>, \<main>, \<footer\>)
* Internal and external links
* Images
* Tables
* Nested tags

---

## Option 3 - **The Topic Explorer**

**Goal:** Choose any topic you love (football, anime, cooking, cars, travel, pets, etc.) and build a mini‑site exploring it.

Pages to Create;

1. overview.html - **Introduction to My Topic**
    * Explain the topic
    * Add at least one image
    * Add a list of subtopics
    * Link to details.html and gallery.html
    * Form **Tell me your favourite item in this topic**
      * Reason text area
      * Dropdown to select favourite topic
      * Name
      * Email
      * Submit button
2. details.html - **Deep Dive**
    * A table comparing 3-5 items related to the topic
        * Example: comparing football teams, anime series, recipes, car models
    * Add nested tags inside table cells
    * Add external links for further reading
    * Link back to overview and gallery
3. gallery.html - **Image Gallery**
    * Add at least 4 images
    * Each image must be wrapped in a link
      html
      \<a href="details.html"\>\<img src="..." alt="..."\>\</a\>
        * Include a caption under each image
    * Link back to the other pages

Required HTML Features;

* Internal navigation
* Images wrapped in links
* Tables
* Nested tags
* Lists

---

## Helpful References & Cheat Sheets for Students

* HTML Cheat Sheets
    * MDN HTML Element Reference (best for beginners): https://developer.mozilla.org/en-US/docs/Web/HTML
    * W3Schools HTML Tags List: https://www.w3schools.com/tags/default.asp
    * HTML Cheat Sheet (printable): https://htmlcheatsheet.com/
* Image Resources
    * Placeholder images: https://picsum.photos
    * Placeholder profile photos: https://randomuser.me
* HTML Validators
    * W3C Validator (to check their code): https://validator.w3.org/

## Follow up lab

Once you have completed this lab, the next stage will be to learn CSS to stylise your page.

[CSS Lab](../CSS/lab1.md)