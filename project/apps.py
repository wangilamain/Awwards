from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = ('project')

    def ready(self):
        import project.signals
