from django.conf.urls import include
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'gametypes', GameTypeView, 'gametype')
# router.register(r'games', GameView, 'game')
# router.register(r'events', EventView, 'event')
# router.register(r'profile', Profile, 'profile')


urlpatterns = [
    path('', include(router.urls)),
    # path('register', register_user),
    # path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('levelupreports.urls')),
]


