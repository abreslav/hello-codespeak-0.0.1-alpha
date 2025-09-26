from django.shortcuts import render
import logging
import json
import time
from django.utils import timezone

logger = logging.getLogger(__name__)

def home(request):
    """Home view that displays the greeting message."""
    start_time = time.time()

    # Log the incoming request
    request_log = {
        "method": request.method,
        "url": request.get_full_path(),
        "headers": dict(request.headers),
        "body_size": len(request.body) if hasattr(request, 'body') else 0,
        "timestamp": timezone.now().isoformat()
    }

    response = render(request, 'django_app/home.html')

    # Log the response
    end_time = time.time()
    processing_time = (end_time - start_time) * 1000  # Convert to milliseconds

    response_log = {
        "request": request_log,
        "response": {
            "status": response.status_code,
            "headers": dict(response.items()) if hasattr(response, 'items') else {},
            "body_size": len(response.content) if hasattr(response, 'content') else 0,
            "processing_duration_ms": processing_time
        }
    }

    logger.info(json.dumps(response_log))

    return response
