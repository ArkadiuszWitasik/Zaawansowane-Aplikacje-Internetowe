from django.apps import AppConfig


class BumboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bumbox'

    def ready(self):
        import bumbox.singals