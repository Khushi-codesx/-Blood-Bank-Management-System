from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('django-admin/', admin.site.urls),
    path('admin/',admin.site.urls),
    path('', include('core.urls')),
]


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('core.urls')),
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












