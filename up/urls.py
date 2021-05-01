from django.urls import path
from . import views
from aishu1 import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='home'),
    path('upload',views.upload.as_view(),name='upload'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)