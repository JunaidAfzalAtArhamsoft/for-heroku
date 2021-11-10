from django.urls import path
from . import views

app_name = 'ManageTask'
urlpatterns = [
    path('register/', views.PersonFormView.as_view(), name='register'),
    path('tasks/', views.TaskView.as_view(), name='task_view'),
    path('add-task/', views.TaskCreateView.as_view(), name='add_task'),
    path('login/', views.PersonLoginView.as_view(), name='login'),
    path('logout/', views.PersonLogoutView.as_view(), name='logout'),
    path('', views.MainPageView.as_view(), name='main_page'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('update/<int:pk>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('tasks/<int:pk>/',  views.SpecificTaskView.as_view(), name='specific_task')
]
