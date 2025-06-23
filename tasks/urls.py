from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("admin", admin.site.urls),
    path("<str:name>", views.index, name='index'),
    path("<int:tasks_id>", views.task, name='task')
]