from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'

    def ready(self):
        import authenticate.signals  # Import signals when the app starts