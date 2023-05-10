from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('signup',views.signup,name='signup'),
   path('logins',views.logins,name='logins'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('showstudent',views.showstudent,name='showstudent'),
   path('signfun',views.signfun,name='signfun'),
   path('logfun',views.logfun,name='logfun'),
   path('logoutfun',views.logoutfun,name='logoutfun'),
   path('addcfun',views.addcfun,name='addcfun'),
   path('stufun',views.stufun,name='stufun'),
   path('showfun',views.showfun,name='showfun')
]
