// secure-server.js
const express = require("express");
const helmet = require("helmet");

const app = express();

// Enable Helmet (all default protections)
app.use(helmet());

app.get("/", (req, res) => {
  res.send("Helmet is ON — security headers are active.");
});

app.listen(3000, () => {
  console.log("Secure server running on http://localhost:3000");
});
