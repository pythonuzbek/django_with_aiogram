from django.urls import path
from .views import CategoryApiView, ProductApiView, UserApiView, CategoryUpdateView

urlpatterns = [
    path('categories',CategoryApiView.as_view()),
    path('products',ProductApiView.as_view()),
    path('user',UserApiView.as_view()),
    path('category/<int:id>',CategoryUpdateView.as_view())
]