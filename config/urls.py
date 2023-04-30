from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views import defaults as default_views

urlpatterns = [
    path(
        "",
        default_views.permission_denied,
        kwargs={"exception": Exception("Permission Denied")},
        name="home",
    ),
    # Url Config
    path(
        "todo/auth/",
        include("todo.authorization.urls", namespace="authorization"),
    ),
    path(
        "todo/operations/",
        include("todo.operations.urls", namespace="authorization"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
