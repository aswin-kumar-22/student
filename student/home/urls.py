from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('enquery/',views.Enquery.as_view(),name='enquery'),
    path('showstudent/',views.Showstudent.as_view(),name='showstudent'),
    path('showstaff/',views.Showstaff.as_view(),name='showstaff'),
    path('edit/',views.Edit.as_view(),name='edit'),
    path('delete/',views.Delete.as_view(),name='delete'),
    path('enquery/',views.Enquery.as_view(),name='enquery'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
    path('form/',views.Form.as_view(),name='form'),
]