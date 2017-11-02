from django.conf.urls import include, url
from django.contrib import admin
from instructors import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'psutinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/$',views.results,name="results"),
    url(r'^$',views.home,name="home"),
    url(r'^instructor/(?P<id>[0-9]+)/$',views.instructor,name="instructor"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
