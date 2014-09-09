from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from stocks.restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'stocks.views.home' , name='home'),

    url(r'^category/$', 'stocks.views.category' , name='category'),
    url(r'^category/(?P<category_name>[-\w\ ]+)$', 'stocks.views.view_category' , name='view_category'),

    url(r'^companies/$', 'stocks.views.companies' , name='companies'),  #show companies
    url(r'^company/add$', 'stocks.views.add_company' , name='add_company'), #add companies
    url(r'^companies/(?P<company_name>[-\w\ ]+)/$', 'stocks.views.view_company', name='view_company'),
    url(r'^companies/(?P<company_name>[-\w\ ]+)/edit$', 'stocks.views.edit_company', name='edit_company'),
    url(r'^companies/(?P<company_name>[-\w\ ]+)/funding$', 'stocks.views.add_funding', name='add_funding'),

    url(r'^profile/$', 'stocks.views.profile', name='profile'),
    url(r'^profile/(?P<profile_username>\w+)$', 'stocks.views.profile_username', name='profile_username'),
    url(r'^contact/$', 'stocks.views.contact', name='contact'),

    url(r'^search/$', 'stocks.views.search', name='search'),
    url(r'^show_company/$', 'stocks.views.show_company' , name='show_company'),  #show companies

    url(r'^register/$', 'stocks.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    #  REST FRAMEWORK
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # USER AUTHENTICATION
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)