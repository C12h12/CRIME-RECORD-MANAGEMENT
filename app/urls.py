from django.contrib import admin
from django.urls import path 
from .import views
from app import views 


urlpatterns = [
    path('',views.start,name='start'),
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('login/citizens',views.login_citizens,name='login_citizens'),
    path('login/police',views.login_police,name='login_police'),
    path('home/',views.home,name='home'),
    path('home_police/',views.home_police,name='home_police'),
    path('logout/',views.logout_view,name='logout'),
    path('logout_police/',views.logout_police,name='logout_police'),
    path('insertuser/',views.insertuser,name='insertuser'),
    path('data/',views.retrieve_data, name='retrievedata'),
    path('dap/',views.analyze_data, name='analyzedata')
]
