from __future__ import annotations

from django.http import HttpRequest, HttpResponse


class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # In case of pre-flight requests or health check request - send empty successful responses
        if (request.method == "OPTIONS" and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META) or \
                request.path == '/health-check':
            return self._send_empty_success_response()
        response = self.get_response(request)
        return self._add_response_headers(response)

    @staticmethod
    def _add_response_headers(response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Expose-Headers"] = "*"
        return response

    @staticmethod
    def _send_empty_success_response():
        response = HttpResponse()
        response["Content-Length"] = "0"
        return AppMiddleware._add_response_headers(response)

        # ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
        # ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
        # ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
        # ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
        # ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
        # ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
