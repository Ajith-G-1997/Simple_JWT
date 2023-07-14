from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from books.views import BookViewSet

# router = DefaultRouter()
# router.register('books', BookViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('',include('books.urls'))
]
