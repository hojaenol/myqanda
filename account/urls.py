from django.conf.urls import url

from account.views import UserAPIView, LoginAPIView

urlpatterns = [
    url(r'^$', UserAPIView.as_view()),
    url(r'login', LoginAPIView.as_view()),
]