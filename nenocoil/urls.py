from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^invoice/', include('invoice.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^profile/', include('profile_page.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),


]
