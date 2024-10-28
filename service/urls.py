from django.urls import path
from .views import service_list, ServiceView, SuperUserView

urlpatterns = [
    path("list-service/", ServiceView.as_view()),
    path("super-list-service/", SuperUserView.as_view()),
    path("new-service/", ServiceView.as_view()),
]
