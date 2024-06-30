from django.urls import path
from .views import *

app_name= 'accounts'
urlpatterns =[
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('signup/', signup_view, name = 'signup'),
    path('signup2/', inputUserPosition, name = 'signup2'),
    path('signup3/', inputUserOpen, name = 'signup3'),
    path('signcomplete/', signComplete, name = 'signcomplete'),
]


