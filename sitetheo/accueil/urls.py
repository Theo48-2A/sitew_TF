from django.urls import path
from .views import home, formation, experience, competences

urlpatterns = [
    path('', home, name='home'),
    path('formation/', formation, name='formation'),
    path('experience/', experience, name='experience'),
    path('competences/', competences, name='competences'),
]
