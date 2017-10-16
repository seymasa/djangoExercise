from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    # Sürekli renderdan cagırmak yerine okunabilirliği de bir nebze arttırabilmek adına ID yi bir değişkende tutacagım...
    if request.user.is_authenticated(): #kullanıcı girişi yapılıp yapılmadıgını kontrol ediyorum...
        context = {
            'ID': 'Seyma Sarıgil'
        }
    else:
        context ={
            'ID': 'GUEST'
        }
    return render(request, 'home.html', context)
    #return render(request, 'home.html', {'ID':'Şeyma Sarıgil'}) #1. parametre daima request, 2.parametre servis edecegimiz html sayfasının adı, 3. view a gönderilecek içerik çiftleri...