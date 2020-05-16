from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from api_v1.user_profile.UserProfileView import UserProfileView
from api_v1.task_view.TaskView import TaskView

router = routers.DefaultRouter()
router.register('v1/user_profile', UserProfileView, basename="UserProfile")
router.register('v1/tasks', TaskView, basename="Tasks")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # url(r'^api/v1/user_profile', UserProfileView),
    url(r'^api/v1/auth_login/', UserProfileView.auth_login),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
