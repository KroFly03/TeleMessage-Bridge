from django.conf import settings
from django.urls import path, include

from docs.swagger import schema_view

urlpatterns = [
    path('api/users', include('users.urls.users')),
    path('api/auth', include('users.urls.auth')),
    path('api/bot', include('bot.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('swagger', schema_view.with_ui('swagger', cache_timeout=0))]
