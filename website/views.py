from django.shortcuts import render, redirect
from django.views import View

from website.models import Website

def redirect_to(request, short: str):
    site = Website.objects.filter(short_url=short).first()
    if site == None:
        ex = f'Website not registered in the database: {short}'
        raise Exception(ex)
    print('Redirecting to: ' + site.full_url)
    return redirect(site.full_url)

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'form.html', {})

    def post(self, request):
        full_url = request.POST['full_url']
        lookup = Website.objects.filter(full_url=full_url)
        if lookup.exists():
            site = Website.objects.get(full_url=full_url)
            return render(request, 'form.html', {'full': full_url, 'short': site.short_url})
        site = Website(full_url=full_url)
        site.save()
        return render(request, 'form.html', {'full': full_url, 'short': site.short_url})
