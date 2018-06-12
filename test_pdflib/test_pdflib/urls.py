
from django.conf.urls import url
from django.contrib import admin

# from apps.pdfcreator.views import PdfView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^responce/', PdfView.as_view),
]
