from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls', namespace='index')),
    path('posts/<int:id>/', include('blog.urls', namespace='post_detail')),
    path(
        'category/<slug:category_slug>/',
        include('blog.urls',
                namespace='category_posts')),
    path('pages/about/', include('pages.urls', namespace='about')),
    path('pages/rules/', include('pages.urls', namespace='rules')),
]