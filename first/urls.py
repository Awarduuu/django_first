from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="page_main"),
    path('one/', views.one, name="page_one"),
    path('two/', views.two, name="page_two"),
    path('one/one_1/', views.one_1, name="page_one_1"),
    path('one/one_2/', views.one_2, name="page_one_2"),
    path('one/one_3/', views.one_3, name="page_one_3"),
    path('two/two_1/', views.two_1, name="page_two_1"),
    path('two/two_2/', views.two_2, name="page_two_2"),
    path('two/two_3/', views.two_3, name="page_two_3"),
]
