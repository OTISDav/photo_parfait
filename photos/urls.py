from django.urls import path
from .views import upload_photos, best_photos

urlpatterns = [
    path('upload/', upload_photos, name='upload_photos'),
    # path('best/', best_photos, name='best_photos'),
    path('best/<str:event_id>/', best_photos, name='best_photos'),
]
