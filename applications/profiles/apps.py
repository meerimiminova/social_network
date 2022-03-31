from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.profiles'

    def ready(self):
        import applications.profiles.signals
