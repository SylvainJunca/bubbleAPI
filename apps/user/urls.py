from django.urls import path


from apps.user import views

user_patterns = [
    path("", views.UserListView.as_view(), name="user-list"),
    path("<uuid:pk>/", views.UserDetailView.as_view(), name="user-detail"),
]
