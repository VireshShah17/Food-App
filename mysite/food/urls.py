# Import the path function from Django's urls module
from django.urls import path
from . import views

app_name = 'food' # naming our app

# Define the URL patterns for the app
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetailView.as_view(), name='detail'),
    path('additem/', views.add_item, name='add_item'),
    path('edititem/<int:item_id>/', views.edit_item, name='edit_item'),
    path('deletitem/<int:item_id>', views.delete_item, name='delete_item'),
]
