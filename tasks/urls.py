from django.urls import path
from .views import TaskAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskDetailAPIView.as_view(), name='task_list_url'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail_url')
]
