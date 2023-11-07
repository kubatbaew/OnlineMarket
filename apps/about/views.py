from django.shortcuts import render

from apps.settingswebsite.models import SettingsWebsite
from apps.about.models import About, TeamMember

def about_page(request):
    settings_website = SettingsWebsite.objects.get(id=1)
    
    about = About.objects.get(id=1)
    
    team_members = TeamMember.objects.all()[:4]
    
    return render(request, "about.html", locals())
