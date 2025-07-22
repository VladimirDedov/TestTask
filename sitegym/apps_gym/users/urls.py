from rest_framework.routers import DefaultRouter
from .views.user_viewset import UserViewSet
from .views.trainer_viewset import TrainerProfileViewSet
from .views.client_viewset import ClientProfileViewSet
from .views.trainer_schedule_viewset import TrainerBookingViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'trainers', TrainerProfileViewSet, basename='trainer')
router.register(r'clients', ClientProfileViewSet, basename='client'),
router.register(r'trainer-bookings', TrainerBookingViewSet, basename='trainer-bookings')

urlpatterns = router.urls