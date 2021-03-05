ICE is short for _Ingress Custom Errors_, and provides a backend which responds to the Nginx headers provided when proxying to a custom error backend. ICE is meant to replace the `default-http-backend` service specified in the `nginx-ingress-controller` deployment arguments.

Expected headers:

- `X-Code`
- `X-Format`
