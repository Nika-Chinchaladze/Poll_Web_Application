from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index-page"),
    path("edit/<str:about>", views.edit_information, name="edit-information"),
    path("delete/<int:user_id>", views.delete_user, name="delete-user"),
    path("register", views.register_user, name="register-user"),
    path("login", views.login_user, name="login-user"),
    path("logout", views.logout_user, name="logout-user"),
    path("personal", views.personal_page, name="personal-page"),
    path("message/<int:user_id>", views.message_page, name="message-page"),
    path("warned/<str:user_name>", views.delete_warned_user, name="delete-warned-user")
]
