import flask
from flask import request, Response, json
import base64
import jsonpatch
import yaml
# import os

response_msgs = {
    "100": "100 Continue",
    "101": "101 Switching Protocols",
    "200": "200 OK",
    "201": "201 Created",
    "202": "202 Accepted",
    "203": "203 Non",
    "204": "204 No Content",
    "205": "205 Reset Content",
    "206": "206 Partial Content",
    "300": "300 Multiple Choices",
    "301": "301 Moved Permanently",
    "302": "302 Found",
    "303": "303 See Other",
    "304": "304 Not Modified",
    "305": "305 Use Proxy",
    "307": "307 Temporary Redirect",
    "400": "400 Bad Request",
    "401": "401 Unauthorized",
    "402": "402 Payment Required",
    "403": "403 Forbidden",
    "404": "404 Not Found",
    "405": "405 Method Not Allowed",
    "406": "406 Not Acceptable",
    "407": "407 Proxy Authentication Required",
    "408": "408 Request Timeout",
    "409": "409 Conflict",
    "410": "410 Gone",
    "411": "411 Length Required",
    "412": "412 Precondition Failed",
    "413": "413 Request Entity Too Large",
    "414": "414 Request",
    "415": "415 Unsupported Media Type",
    "416": "416 Requested Range Not Satisfiable",
    "417": "417 Expectation Failed",
    "494": "494 Nginx internal",
    "495": "495 Nginx internal",
    "500": "500 Internal Server Error",
    "501": "501 Not Implemented",
    "502": "502 Bad Gateway",
    "503": "503 Service Unavailable",
    "504": "504 Gateway Timeout",
    "505": "505 HTTP Version Not Supported",
}

ice = flask.Flask(__name__)

@ice.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def handle():

    # typically available headers:
    #   X-Code
    #   X-Format
    #   X-Original-URI
    #   X-Namespace
    #   X-Ingress-Name
    #   X-Service-Name
    #   X-Service-Port
    #   Host

    response_code = request.headers.get("X-Code") if request.headers.has_key("X-Code") else "500"
    response_msg = response_msgs[response_code] if response_code in response_msgs else (response_code + " Unknown")
    response_format = request.headers.get("X-Format")

    if "application/json" == response_format:
        return Response(json.dumps({"message":response_msg}), status=response_code, content_type="application/json")
    else:
        return Response(response_msg, status=response_code, content_type="text/plain")

if __name__ == '__main__':
    ice.run(host='0.0.0.0', port=8080)
