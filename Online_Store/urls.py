"""
URL configuration for Online_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from product.views import HelloCBV, NowdateCBV, GoodbyCBV, MainCBV, ProductsCBV, ProductCreateCBV, ProductDetailCBV
from users.views import RegisterCBV, LoginCBV, LogoutCBV
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloCBV.as_view()),
    path('now_date/', NowdateCBV.as_view()),
    path('goodby/', GoodbyCBV.as_view()),
    path('', MainCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('products/create/', ProductCreateCBV.as_view()),
    path('products/<int:id>/', ProductDetailCBV.as_view()),

    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

