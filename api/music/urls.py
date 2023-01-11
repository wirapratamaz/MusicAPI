from django.urls import path
from .views import ListSongsView

urlpatterns = [
    #as_view() method is used to convert the view class into a callable view 
    #function that can handle requests.
    path('songs/', ListSongsView.as_view(), name="songs-all")
]