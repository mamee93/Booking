from django.urls import path
from . import views

app_name= 'posts'

urlpatterns = [
    path('',views.post_list, name='post_list'),
    # path('update_list/<str:pk>/',views.updateList, name='update_list'),
    # path('delete/<str:pk>/',views.deleteList, name='delete_list'),
]
