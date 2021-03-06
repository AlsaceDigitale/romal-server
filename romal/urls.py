"""romal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from challenges import viewsets as challenges_viewsets
from users import viewsets as users_viewsets

router = DefaultRouter()
router.register(r'challenges', challenges_viewsets.ChallengeViewSet)
router.register(r'running-challenges', challenges_viewsets.RunningChallengeViewSet)
router.register(r'users', users_viewsets.UserViewSet)
router.register(r'scores', challenges_viewsets.ScoreViewSet)
router.register(r'game-status', challenges_viewsets.GameStatusViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    url(r'api/', include(router.urls)),
]
