from django.shortcuts import render, redirect
from .models import Osat, Autot
from django.contrib.auth import authenticate, login, logout

#def etusivuview(request):
#    return render (request, 'etusivu.html')

#Login ja logout

def loginview(request):
     return render (request, "loginpage.html")

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        login(request, user)
        context = {'name': user.first_name}
        return render(request,'etusivu.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

#Osat

def osatview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        osat = Osat.objects.all()
        autot = Autot.objects.all()
        context = {'osat': osat, 'autot': autot}
        return render (request, 'osat.html', context)

def addosat(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        a = request.POST['tuotenimi']
        b = request.POST['paino']
        c = request.POST['määrä']
        d = request.POST['hinta']
        e = request.POST['auto']
    
        Osat(tuotenimi=a, paino=b, määrä=c, hinta=d, auto=Autot.objects.get(id=e)).save()

        return redirect(request.META['HTTP_REFERER'])

def edit_osat(request, id):
    osat = Osat.objects.get(id = id)
    context = {'osat': osat}
    return render (request, "osatedit.html", context)


def edit_osat_post(request, id):
    item = Osat.objects.get(id = id)
    item.määrä = request.POST['määrä']
    item.hinta = request.POST['hinta']
    item.save()
    return redirect(osatview)

def deleteosat(request, id):
    Osat.objects.get(id = id).delete()
    return redirect(osatview)


def confirmdeleteosat(request, id):
    osat = Osat.objects.get(id = id)
    context = {'osat': osat}
    return render (request,"osatdel.html",context)

def searchosat(request):
    search = request.POST['search']
    filtered = Osat.objects.filter(tuotenimi__icontains=search)
    context = {'osat': filtered}
    return render (request,"osat.html",context)

#Autot

def autotview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        autot = Autot.objects.all()
        context = {'autot': autot}
        return render (request, 'autot.html', context)

def addautot(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        a = request.POST['merkki']
        b = request.POST['malli']
        c = request.POST['vuosi']
        d = request.POST['väri']
        e = request.POST['moottori']
        f = request.POST['hinta']
        Autot(merkki = a, malli = b, vuosi = c, väri = d, moottori = e, hinta = f).save()
        return redirect(request.META['HTTP_REFERER'])

def edit_autot(request, id):
    autot = Autot.objects.get(id = id)
    context = {'autot': autot}
    return render (request, "autotedit.html", context)


def edit_autot_post(request, id):
    item = Autot.objects.get(id = id)
    item.moottori = request.POST['moottori']
    item.hinta = request.POST['hinta']
    item.save()
    return redirect(autotview)

def deleteautot(request, id):
    Autot.objects.get(id = id).delete()
    return redirect(autotview)


def confirmdeleteautot(request, id):
    autot = Autot.objects.get(id = id)
    context = {'autot': autot}
    return render (request,"autotdel.html",context)

def searchautot(request):
    search = request.POST['search']
    filtered = Autot.objects.filter(merkki__icontains=search)
    context = {'autot': filtered}
    return render (request,"autot.html",context)
