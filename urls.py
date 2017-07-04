from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^example$', 'tutorons.modules.java_classes.views.example', name='example'),
    url(r'^scan$', 'tutorons.modules.java_classes.views.scan', name='scan'),
)
