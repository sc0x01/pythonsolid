from django.contrib import admin
from django.urls import path
from django.shortcuts import reverse
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap

from .views import home, about, projects, contact  # View fonksiyonlarını içe aktar

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'projects', 'contact']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
]
