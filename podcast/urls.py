from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

# from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view

from users import views as user_views

# API_TITLE = 'Podcast API via CoreAPI'
# API_DESCRIPTION = 'Description'
# schema_view = get_schema_view(title='Podcast API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html/'),
         name='login'
         ),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html/'),
         name='logout'
         ),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html/'),
         name='password_reset'
         ),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html/'),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html/'),
         name='password_reset_confirm'
         ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html/'),
         name='password_reset_complete'
         ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('coupons', include('coupons.urls', namespace='coupons')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
    #     path('silk/', include('silk.urls', namespace='silk')),
#     path('api/v1/', include('api.urls')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/v1/rest-auth/', include('rest_auth.urls')),
#     path('api/v1/rest-auth/registration/',  # new
     #     include('rest_auth.registration.urls')),
#     path('docs/', include_docs_urls(title=API_TITLE,
                                   #  description=API_DESCRIPTION)),
#     path('schema/', schema_view),
    path('', include('blog.urls', namespace='podcast')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
