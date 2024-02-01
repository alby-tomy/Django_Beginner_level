from . import views
from django.urls import include, path

app_name = 'todo_app'

urlpatterns = [
    path('', views.addView, name='index'),
    # path('details',views.detailView, name='detailName'),
    path('delete/<int:itemId>', views.deleteView, name='deleteName'),
    path('update/<int:itemId>', views.updateView, name='updateName'),
    path('cbvhome/',views.TaskListView.as_view(), name='cbvhomeName'),
    path('ddd/<int:pk>',views.TaskDetailView.as_view(),name='dddName'),
    path('uuu/<int:pk>',views.TaskUpdateView.as_view(), name='uuuName'),
    path('del/<int:pk>',views.TaskDeleteView.as_view(), name='delName'),
]
