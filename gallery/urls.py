from django.conf.urls import url
from . import views


urlpatterns = [
    url('',views.home,name='today'),
    url('about/', views.about, name='about'),
    url('search/', views.search_results, name='search_results'),
    url('image/<int:image_id>', views.view_image,name='view_image'),
    url('category/<int:id>', views.category,name='category')
]