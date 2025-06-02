"""
URL configuration for galanterka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from eshop.views.produkty.index import index
from eshop.views.produkty.delete import delete

handler404 = "galanterka.views.custom_404"

urlpatterns = [
    path('', index, name='produkty_seznam'),
    path('eshop/<int:produkt_id>/odstranit/', delete, name='produkt_smazat'), # propojení URL v template s view pro smazání produktu
]
