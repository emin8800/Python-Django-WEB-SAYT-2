from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    BlogView,
    BlogDetailApiView,
    SubsciberApiView,
    BasketApiView,

)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', BlogDetailApiView.as_view(), name='blog_details'),
    path('subscriber/', SubsciberApiView.as_view(), name='subscriber'),
    path('basket/', BasketApiView.as_view, name='basket'),
]
    