from .views import UserViewSet, TripViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    # ...
]

router.register('user', UserViewSet, basename='user')
router.register('trip', TripViewSet, basename='trip')

urlpatterns = router.urls