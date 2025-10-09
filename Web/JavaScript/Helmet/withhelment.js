const express = require('express');
const helmet = require('helmet');
const csp = require('helmet-csp');

const app = express();

app.use(helmet()); // basic Helmet protections

// Use helmet middleware with Content Security Policy
app.use(csp({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'"]
  }
}));

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.listen(3002, () => {
  console.log('Server is running on port 3002');
});