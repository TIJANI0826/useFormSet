# app level urls.py
from django.urls import path
from .views import BirdAddView, BirdListView,BirdDetail,BirdDelete,EditBird

urlpatterns = [
    path('add', BirdAddView.as_view(), name="add_bird"),
    path('', BirdListView.as_view(), name="bird_list"),
    path('update/<int:pk>', EditBird.as_view(), name='bird_update'),
    path('delete/<int:pk>', BirdDelete.as_view(), name='bird_delete'),
    path('bird/<int:pk>', BirdDetail.as_view(), name='bird_detail'),
]

#  path('', views.BookList.as_view(), name='book_list'),
#     path('book_create', views.CreateBook.as_view(), name='book_create'),
#     path('update/<int:pk>', views.EditBook.as_view(), name='book_update'),
#     path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
#     path('book/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
