# This example shows what happens when Helmet is not used.

## What happens here

Without Helmet, your server:
- Does not set X-Frame-Options → vulnerable to clickjacking
- Does not set X-Content-Type-Options → MIME sniffing risk
- Does not set Content-Security-Policy → easier XSS attacks
- Does not set Referrer-Policy → leaks more user info

Run it:

```
node insecure-server.js
```

Compare the headers with the secure version — you'll see the difference immediately.