"""game_streaming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from game_streaming import views

urlpatterns = [
    path('', views.index, name='index'),
    path('market/', views.market, name='market'),
    path('user/library/', views.user_library, name='user_library'),
    re_path(r'^user/library/(?P<game_id>\w+)/$', views.user_library_game, name='user_library_game'),
    re_path(r'^user/library/add/(?P<game_id>\w+)/$', views.user_library_add_game, name='user_library_add_game'),
    re_path(r'^run/(?P<game_id>\w+)/$', views.run_game, name='run_game'),

    # Administration site
    path('admin/', admin.site.urls),

    # User authentication
    path('user/login/', auth_views.LoginView.as_view(template_name='game_streaming/login.html'), name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/register/', views.register, name='register'),
]
