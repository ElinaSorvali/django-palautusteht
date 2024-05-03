from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import osatview, autotview, addosat, addautot, edit_osat, edit_osat_post, \
    edit_autot, edit_autot_post, deleteosat, confirmdeleteosat, deleteautot, confirmdeleteautot, searchautot, \
    searchosat, loginview, login_action, logout_action

urlpatterns = [
   # path('etusivu/', etusivuview),

    #Loginview ja authentication
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    #osat
    path('osat/', osatview),
    path('add-osat/', addosat),
    path('edit-osat/<int:id>/', edit_osat),
    path('edit-osat-post/<int:id>/', edit_osat_post),
    path('delete-osat/<int:id>/', deleteosat),
    path('confirm-delete-osat/<int:id>/', confirmdeleteosat),
    path('search-osat/', searchosat),


    #autot
    path('autot/', autotview),
    path('add-autot/', addautot),
    path('edit-autot/<int:id>/', edit_autot),
    path('edit-autot-post/<int:id>/', edit_autot_post),
    path('delete-autot/<int:id>/', deleteautot),
    path('confirm-delete-autot/<int:id>/', confirmdeleteautot),
    path('search-autot/', searchautot),

]
urlpatterns += staticfiles_urlpatterns()