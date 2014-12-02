from django.conf.urls import patterns, include, url
from django.contrib import admin
from VideoCMS.views import video_player, video_download
import VideoCMS

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PySharpVideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^VideoCMS/', include(VideoCMS))
)

