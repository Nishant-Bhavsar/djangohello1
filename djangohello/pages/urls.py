from django.urls import path
from pages import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('about/', views.about),
]
