// secure-server.js
const express = require("express");
const helmet = require("helmet");

const app = express();

// Strict CSP: only allow images from *this* server
app.use(
  helmet.contentSecurityPolicy({
    useDefaults: true,
    directives: {
      "img-src": ["'self'"], // block all external images
    },
  })
);

app.get("/", (req, res) => {
  res.send(`
    <h1>Helmet CSP Demo</h1>
    <p>Below is an image from your server (allowed):</p>
    <img src="/local-image.png" width="200" />

    <p>Below is an image from another domain (blocked):</p>
    <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo-1536x864.png" width="200" />
  `);
});

// Serve a local image
app.get("/local-image.png", (req, res) => {
  res.sendFile(__dirname + "/local-image.png");
});

app.listen(3000, () => {
  console.log("Secure server running on http://localhost:3000");
});
