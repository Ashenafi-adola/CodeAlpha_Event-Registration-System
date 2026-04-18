from django.urls import path
from . views import Home, Registration, EventDetail
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', LoginView.as_view(template_name='core/authPage.html'), name="login"),
    path('register/', Registration.as_view(), name='signup'),
    path('signout/', LogoutView.as_view(template_name='core/authPage.html'), name='signout'),
    path('detail/<int:pk>/', EventDetail.as_view(), name='detail')

]
