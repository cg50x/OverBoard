from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_service import views
#from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'columns', views.ColumnViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'boardpermissions', views.BoardPermissionViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Overboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
