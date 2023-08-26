from django.urls import path
from .views import dashboardpost,LoginApiview
urlpatterns = [
    path("dashboardpost/",dashboardpost.as_view()),
    path("login/",LoginApiview.as_view())
]

