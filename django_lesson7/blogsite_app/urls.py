from django.urls import path
from .views import PostListView, post_detail


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail , name='post_detail')
]