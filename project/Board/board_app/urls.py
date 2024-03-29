from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail'),
    path('schedule', views.schedule, name='schedule'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)