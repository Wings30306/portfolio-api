from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from portfolio.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"languages", views.LanguageViewSet)
router.register(r"projectlanguages", views.ProjectLanguageViewSet)
router.register(r"courses", views.CourseViewSet)



# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
]
