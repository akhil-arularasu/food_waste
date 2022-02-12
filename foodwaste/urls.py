"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from foodwaste.views import IndexView,CountryLevelWasteView,CountryDetailView,CountryChartView,PledgeResultsView

urlpatterns = [
      path('', CountryChartView.as_view(), name='CountryChartView'),
      path('<int:pk>/',CountryDetailView.as_view(),name='detail'),
      path('compost', views.compost, name='compost'),
      path('compost-school', views.compostschool, name='compostschool'),
      path('compost-demo', views.compostdemo, name='compostdemo'),
      path('milltown-school', views.milltownschool, name='milltownschool'),
      path('pledge', views.pledge_info_view, name='pledge_info'),
      path('pledgeresults', PledgeResultsView.as_view(), name='pledge_results'),
      path('about', views.about, name='about'),
      path('press-coverage', views.press_coverage, name='press-coverage'),
      path('foodwaste-report', views.foodwaste_report, name='foodwaste_report'),
      path('Research_At_RVCC', views.Research_At_RVCC, name='Research_At_RVCC'),
      path('foodwaste-report', views.foodwaste_report, name='foodwaste_report'),
      path('classify-waste', views.classify_waste_view, name='classify_waste'),
]
