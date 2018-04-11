from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from desayunos import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/v1/User/', views.UserViewSet)
router.register('api/v1/Bar/', views.BarViewSet)
router.register('api/v1/User/Group', views.GroupViewSet, base_name='group')
router.register('api/v1/ProductType/', views.ProductTypeViewSet)
router.register('api/v1/ProductType/Product', views.ProductViewSet)
router.register('api/v1/Bar/Menu', views.MenuViewSet)
router.register('api/v1/Modifier', views.ModifierViewSet)
#router.register('Pivot', views.PivotModifierProductViewSet)
router.register('api/v1/Group/Bar/Order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/User/Register/', views.user_register, name='register'),
    path('api_auth/auth-jwt/', obtain_jwt_token),
    path('api_auth/auth-jwt-verify/', verify_jwt_token)
]
