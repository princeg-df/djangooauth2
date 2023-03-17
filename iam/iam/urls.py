from django.contrib import admin
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from users.views import UserList

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'file/', include('users.urls')),
    re_path('users/', UserList.as_view()),

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)