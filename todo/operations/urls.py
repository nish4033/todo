from django.urls import path

from . import views

app_name = "call"

urlpatterns = [
    path("add_task", view=views.TodoAPIView.as_view(), name="add_todo"),
    path("get_todo", view=views.TodoDetailsAPIView.as_view(), name="get_todo"),
    path(
        "update_todo/<int:pk>",
        view=views.TodoUpdateAPIView.as_view(),
        name="update_todo",
    ),
]
