

from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.TaskListview.as_view(),name='cbvindex'),
    path('cbvdetale/<int:pk>/',views.TaskDetaleview.as_view(),name='cbvdetale'),
    path('cbvupdate/<int:pk>/',views. TaskUpdateview.as_view(),name='cbvupdate'),
    ] 