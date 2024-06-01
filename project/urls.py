from django.contrib import admin
from django.urls import path , include
from book import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('books' , views.Viewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    # Static (No Models)
    path('no_models/',views.no_models),
    # 2 Model API With Django (With Models)
    path('no_rest/',views.model_api_no_rest),
    # 3.1 FBV
    path('fbv/',views.fbv),
    # 3.2 FBV With GET PUT DELETE
    path('fbv/<int:pk>',views.fbv_pk),
    # 4.1 [CBV] GET POST
    path('cbv/',views.CBV.as_view()),
    # 4.2 [CBV] GET PUT DELETE
    path('cbv/<int:pk>',views.Cbv_Pk.as_view()),
    # 5.1 [mixins] GET POST
    path('mixin/',views.Mixins.as_view()),
    # 5.2 [mixins] GET PUT DELETE
    path('mixin/<int:pk>',views.Mixins_Pk.as_view()),
    # 6.1 [generic] GET POST
    path('generic/',views.Generic.as_view()),
    # 6.2 [generic] GET PUT DELETE
    path('generic/<int:pk>',views.Generic_Pk.as_view()),
    # 7.1 [viewset]
    path('viewset/',include(router.urls)),
    # Rest Auth Url
    path('api-auth/',include('rest_framework.urls')),
    # Token Authentication
    path('api-token-auth/' , obtain_auth_token),
]




