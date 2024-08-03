from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup/', views.UserCreateAndLoginView.as_view(),
         name='signup'),
    path('', LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
        ),
    path(
        'user_detail/<int:pk>/',
        views.UserDetail.as_view(),
        name='detalle_user',
        ),
    path(
        'user_update/<int:pk>/',
        views.UserUpdate.as_view(),
        name='Actualizar_user',
        ),
    path(
        'password_change/',
        views.PasswordChange.as_view(),
        name='Cambiar_password',
        ),
    path(
        'password_change/done/',
        views.PasswordChangeDone.as_view(),
        name='password_change_done',
        ),
    path(
        'user_delete/<int:pk>/',
        views.UserDelete.as_view(),
        name='borrar_user',
        ),
]
