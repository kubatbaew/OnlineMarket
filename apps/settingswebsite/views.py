from django.shortcuts import render

from apps.settingswebsite.models import SettingsWebsite
from apps.categories.models import Category


def homepage(request):
    settings_website = SettingsWebsite.objects.get(id=1)
    category_1 = Category.objects.get(id=1)
    category_2 = Category.objects.get(id=2)
    category_3 = Category.objects.get(id=3)

    return render(request, 'index.html', locals())
