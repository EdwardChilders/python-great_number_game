from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('guess', views.guess),
    path('again', views.again),
]