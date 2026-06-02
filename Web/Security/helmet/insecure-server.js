// insecure-server.js
const express = require("express");
const app = express();

// No Helmet here!

app.get("/", (req, res) => {
  res.send("Helmet is OFF — no security headers.");
});

app.listen(3001, () => {
  console.log("Insecure server running on http://localhost:3001");
});
