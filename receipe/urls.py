from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
  path('home/', views.home, name = "home"),
  path('deleteReceipe/<id>/', views.deleteReceipe, name="deleteReceipe"),
  path('updateReceipe/<id>/', views.updateReceipe, name="updateReceipe"),
  path('login/', views.loginPage, name = "loginPage"),
  path('logout/', views.logoutPage, name = "logoutPage"),
  path('register/', views.registerPage, name = "registerPage"),

]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()