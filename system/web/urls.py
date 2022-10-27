from django.urls import path
from . import views

urlpatterns = [
	path('', views.start, name='start'),
	path('data', views.data, name='data'),
	path('data/create', views.create, name='create'),
	path('data/edit', views.edit, name='edit'),
	path('delete/<int:id>', views.delete, name='delete'),
	path('data/edit/<int:id>', views.edit, name='edit'),
	
]