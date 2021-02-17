from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('interviews/', TemplateView.as_view(template_name = 'index.html'), name="index"),
    path('interviews/<int:pk>', TemplateView.as_view(template_name = 'interview.html'), name="interview"),

    path('admin/', admin.site.urls),
    path('api/', include('rest.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)