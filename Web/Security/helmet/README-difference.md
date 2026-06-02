# The differences

## Using curl.

### Secure headers

```
$ curl -I http://localhost:3000

HTTP/1.1 200 OK
Content-Security-Policy: default-src 'self';base-uri 'self';font-src 'self' https: data:;form-action 'self';frame-ancestors 'self';img-src 'self' data:;object-src 'none';script-src 'self';script-src-attr 'none';style-src 'self' https: 'unsafe-inline';upgrade-insecure-requests
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
Origin-Agent-Cluster: ?1
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-DNS-Prefetch-Control: off
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 0
Content-Type: text/html; charset=utf-8
Content-Length: 45
ETag: W/"2d-RQNH95tWPcvacCYz4/MHVAkricM"
Date: Tue, 02 Jun 2026 20:03:27 GMT
Connection: keep-alive
Keep-Alive: timeout=5
```

### Insecure

```
$ curl -I http://localhost:3001

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 38
ETag: W/"26-2fA1pWWsuvg7OpDGEUm/YwSKnvM"
Date: Tue, 02 Jun 2026 20:04:07 GMT
Connection: keep-alive
Keep-Alive: timeout=5
```


You’ll see Helmet's headers in the secure version and missing in the insecure one.