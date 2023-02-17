from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/edit', UpdatePage.as_view(), name='edit'),
    path('<int:pk>/delete', DeleteNote.as_view(), name='delete-note'),
    path('search/', post_search, name='post_search'),
    # path('/delete-post/', delete_post, name='delete_post'),
]
