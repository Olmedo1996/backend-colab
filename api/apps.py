from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        """
        Overriden ready method to load v2 app models.
        This is necessary because models are referenced in api.urls.
        """
        import api.v2.models 