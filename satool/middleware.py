from django.conf import settings
import time


class TimeDelayMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.delay = settings.DEBUG_REQUEST_TIME_DELAY

    def __call__(self, request):
        if "/api/" in request.path:
            time.sleep(self.delay)
        response = self.get_response(request)
        return response
