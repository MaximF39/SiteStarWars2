from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('Main.urls')),
    path('forum/', include('Forum.urls')),
    path('account/', include('PersonalAccount.urls')),
    path('admin/', admin.site.urls),
]