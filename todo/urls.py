from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('task-list/', views.TaskListView.as_view(), name="tasklist"),
    path('task-list/<int:pk>/', views.TaskDetailView.as_view(), name='taskdetail'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='taskupdate' ),
    path('task-create/', views.TaskCreateView.as_view(), name='taskcreate'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='taskdelete'),

    path('login/', views.OurLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
