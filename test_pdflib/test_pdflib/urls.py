
from django.conf.urls import url
from django.contrib import admin

from apps.pdfcreator.views import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^responce/', view),
    #?user_id={}
]
