from django.urls import path
from .views import recipe_list, recipe_details

app_name = "ledger"

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:id>/', recipe_details, name='recipe_detail'),
]

