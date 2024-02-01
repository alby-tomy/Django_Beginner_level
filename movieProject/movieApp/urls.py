from django.urls import path, include
from . import views

app_name = 'movieApp'
urlpatterns = [
    path('',views.indexName, name='indexName'),
    path('movie/<int:movieId>/',views.detailsView, name='detailsName'),
    path('update/<int:movieId>/',views.updateView, name='updateName'),
    path('addItem/',views.addItemsView,name='addItemName'),
    path('deleteItem/<int:movieId>',views.deleteView, name='deleteName')
]
