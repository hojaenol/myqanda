"""myqanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from contact.views import UserContactViewSet
from notice.views import NoticeViewSet

router = SimpleRouter()
router.register('notice', NoticeViewSet)
router.register('contact', UserContactViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/user/', include('account.urls', namespace='account')),
    url(r'^api/v1/', include('profiles.urls', namespace='profiles')),
]
