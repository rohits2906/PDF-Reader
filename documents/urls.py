# documents/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.LoadDocumentAPI.as_view(), name='document-ingestion'),
    path('api/qa/', views.QuestionAndAnswerAPI.as_view(), name='qa-api'),
]

