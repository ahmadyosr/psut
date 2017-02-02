from django.conf.urls import include, url
from django.contrib import admin
from instructors  import views 
urlpatterns = [
    # Examples:
    # url(r'^$', 'psutinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/$',views.results,name="results"),
    url(r'^home/$',views.home,name="home2"),
    url(r'^instructor/(?P<id>[0-9]+)/$',views.instructor,name="instructor2"),
]
