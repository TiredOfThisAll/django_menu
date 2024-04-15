from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "menu"
urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("food/", views.food, name="food"),
    path("food/fruit/", views.fruit, name="fruit"),
    path("food/vegetables/", views.vegetables, name="vegetables"),
    path("food/berries/", views.berries, name="berries"),
    path("food/fruit/orange/", views.orange, name="orange"),
    path("clothes/", views.clothes, name="clothes"),
    path("clothes/hats/", views.hats, name="hats"),
    path("clothes/tops/", views.tops, name="tops"),
    path("clothes/pants/", views.pants, name="pants"),
    path("clothes/boots/", views.boots, name="boots"),
    path("clothes/hats/ushanka/", views.ushanka, name="ushanka")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)