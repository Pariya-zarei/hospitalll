from django.urls import path
from .views import reserve_view, ReserveView, ReserveDetail

urlpatterns = [
    path('new-reserve/' , ReserveView.as_view()),
    path('list-reserve/' , ReserveView.as_view()),
    path('detail-reserve/<int:pk>' , ReserveDetail.as_view()),
]