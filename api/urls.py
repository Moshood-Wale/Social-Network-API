from django.urls import path, include
from .views import register, login, like, unlike, posts, user_data
from rest_framework.routers import DefaultRouter


app_name = "api"
router = DefaultRouter()
router.register('manage-posts', posts.ManagePostsViewSet, basename='manage-posts')


urlpatterns = [
    path('register/', register.RegisterUserView.as_view(), name='register'),
    path('login/', login.LoginAPIView.as_view(), name='login'),
    path('like/', like.LikeAPIView.as_view(), name='like'),
    path('unlike/', unlike.UnLikeAPIView.as_view(), name='unlike'),
    path('user_data/', user_data.DetailsView.as_view(), name='user_data'),
    path(r'', include(router.urls)),
]
