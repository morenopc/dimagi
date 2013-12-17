from django.conf.urls import patterns, url

from .views import MathEngineView

urlpatterns = patterns('',

    # {% url "math_engine:results-json" %}
    url(
        regex=r'^$',
        view=MathEngineView.as_view(),
        name="results-json"
    ),
)
