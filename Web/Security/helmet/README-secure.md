# This example shows Helmet correctly applied to an Express server.

## What happens here

Helmet automatically adds headers like:
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Strict-Transport-Security (when HTTPS)
- Cross-Origin-Resource-Policy

You can verify by running:

```
node secure-server.js
```

Go to http://localhost:3000

And inspect the response headers in your browser’s DevTools → Network tab.