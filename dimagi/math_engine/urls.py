from django.conf.urls import patterns, url

from .views import MathEngineView, MathEngineChallengeView

urlpatterns = patterns('',

    # {% url "math_engine:results-json" %}
    url(
        regex=r'^$',
        view=MathEngineView.as_view(),
        name="results-json"
    ),

    # {% url "math_engine:challenge-results-json" %}
    url(
        regex=r'^challenge/$',
        view=MathEngineChallengeView.as_view(),
        name="challenge-results-json"
    ),
)
