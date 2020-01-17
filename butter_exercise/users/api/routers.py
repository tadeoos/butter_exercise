from butter_exercise.users.api.views import UserViewSet, AgreementViewSet
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()

users_router = router.register('users', UserViewSet)
users_router.register(
    'agreements', AgreementViewSet,
    basename='user-agreements',
    parents_query_lookups=['user']
)
