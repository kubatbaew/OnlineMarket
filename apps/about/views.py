from django.shortcuts import render

from apps.settingswebsite.models import SettingsWebsite
from apps.about.models import About

def about_page(request):
    settings_website = SettingsWebsite.objects.get(id=1)
    
    about = About.objects.get(id=1)
    
    return render(request, "about.html", locals())
