from django.urls import path
from . import views

# http://127.0.0.1:8000/polls/
# http://127.0.0.1:8000/polls/3/
# http://127.0.0.1:8000/polls/3/results
# http://127.0.0.1:8000/polls/3/vote/

"""the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?
The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:
"""

app_name = "polls"

urlpatterns = [
    # ex: http://127.0.0.1:8000/polls
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]