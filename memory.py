import os
import psutil
import sys

from django.conf import settings

THRESHOLD = 2*1024*1024

class MemoryUsageMiddleware(object):

    def process_request(self, request):
        request._mem = psutil.Process(os.getpid()).get_memory_info()

    def process_response(self, request, response):
        mem = psutil.Process(os.getpid()).get_memory_info()
        diff = mem.rss - request._mem.rss
        if diff > THRESHOLD:
           print >> sys.stderr, 'MEMORY USAGE %r' % ((diff, request.path),)
        return response
