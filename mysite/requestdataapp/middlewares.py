import time

from django.http import HttpRequest
from django.shortcuts import render


def set_useragent_on_request_middleware(get_response):

    print('initial call')

    def middleware(request: HttpRequest):
        print('before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('after get response')
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.request_time = {}

    def __call__(self, request: HttpRequest):
        time_delay = 0
        if not self.request_time:
            print('first request')
        else:
            if (round(time.time()) * 1) - self.request_time['time'] < time_delay \
                    and self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
                        print('Requests limit exceeded')
                        context = {
                            'time_delay': time_delay,
                            'title': 'Requests limit error message',
                            'error_msg': f'Error! The number of requests from your ip-address is exceeded. '
                                         f'Please try later in {time_delay} seconds',
                            'href_msg': f'Please wait {time_delay} sec. and you can return back to page',

                        }
                        return render(request, 'requestdataapp/error-message.html', context=context)
        self.request_time = {'time': round(time.time()) * 1, 'ip_address': request.META.get('REMOTE_ADDR')}

        self.requests_count += 1
        print('requests count', self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print('responses count', self.responses_count)
        return response

    def process_exceptions(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exceptions so far')

