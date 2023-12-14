from django.urls import path
from . import views

urlpatterns = [
    path('marksheet/', views.marksheet, name='marksheet'),
    path('myfirst/', views.myfirst, name='myfirst'),
    path('stud_data/',views.stud_data,name='stud_data'),
    path('insert_data/',views.insert_data,name='insert_data'),
    path('update_data/<int:item_id>', views.update_data, name='update_data'),
    path('delete_data/<int:item_id2>', views.delete_data, name='delete_data'),

    path('search_data/', views.search_data, name='search_data'),
]