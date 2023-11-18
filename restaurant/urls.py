#define URL route for index() view
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    # path('users/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
