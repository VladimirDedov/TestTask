from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness Scheduling API",
        default_version='v1',
        description="""
        API для управления расписанием фитнес-тренеров, клиентами и залами.

        Доступные сущности:
        - **Users** — пользователи (админ, клиент, тренер)
        - **Trainers** — профили тренеров
        - **Clients** — профили клиентов
        - **Gyms** — фитнес-залы
        - **Schedule** — расписание тренировок
        """,
        contact=openapi.Contact(email="admin@fitnessapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
