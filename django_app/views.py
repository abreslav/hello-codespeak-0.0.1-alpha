from django.shortcuts import render
import logging
import json
import time

logger = logging.getLogger('django_app')

def hello(request):
    """
    View to render the hello page with greeting message.
    """
    start_time = time.time()

    # Log the incoming request
    request_data = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
        'method': request.method,
        'url': request.get_full_path(),
        'headers': dict(request.headers),
        'body_size': len(request.body) if request.body else 0,
        'remote_addr': request.META.get('REMOTE_ADDR', 'unknown')
    }

    # Render the template
    response = render(request, 'hello.html')

    # Calculate processing duration
    processing_duration = time.time() - start_time

    # Log the response
    response_data = {
        **request_data,
        'response_status': response.status_code,
        'response_headers': dict(response.items()),
        'response_body_size': len(response.content) if hasattr(response, 'content') else 0,
        'processing_duration_seconds': processing_duration
    }

    logger.info(json.dumps(response_data))

    return response
