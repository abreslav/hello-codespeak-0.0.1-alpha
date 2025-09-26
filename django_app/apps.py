from django.apps import AppConfig
import logging
import atexit


class DjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_app'

    def ready(self):
        """
        Called when the Django app is ready.
        Log server startup and register shutdown handler.
        """
        logger = logging.getLogger('django_app')
        logger.info("Server started successfully")

        # Register shutdown handler
        def shutdown_handler():
            logger.info("Stopping server")

        atexit.register(shutdown_handler)
