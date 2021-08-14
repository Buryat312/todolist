from django.urls import path
from .views import TaskAPIView, TaskFinishedAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task_list_url'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail_url'),
    path('tasks/<int:id>/finished/', TaskFinishedAPIView.as_view(), name='task_finished_url'),
]
