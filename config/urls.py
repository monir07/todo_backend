
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('todo.urls')),
]

# ADMIN PANEL HEADER AND TITLE TEXT CHANGE.
admin.site.site_header = "To-Do Admin"
admin.site.site_title = "To-Do Admin Portal"
admin.site.index_title = "Welcome to To-Do Portal"
