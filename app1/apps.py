from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'app1'
    def ready(self):
        import app1.mysignal
