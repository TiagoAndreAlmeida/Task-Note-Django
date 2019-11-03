from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api_v1.user_profile.UserProfileView import UserProfileView

router = routers.DefaultRouter()
router.register('v1/user_profile', UserProfileView, basename="UserProfile")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
