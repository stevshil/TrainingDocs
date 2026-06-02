# Local and remote images

This example shows how a server trying to serve a remote image not from the server is denied.

Before opening the page in your browser;

1. Open Developer Tools
2. Select Network tab

You'll notice;

- **local-image.png** has no issue
- **image.jpg** does not render and blocked by helmet `"img-src": ["'self'"]`