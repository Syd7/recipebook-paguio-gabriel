from django.urls import path
from .views import recipe_list, recipe_details, add_recipe, add_image
from django.conf import settings
from django.conf.urls.static import static

app_name = "ledger"

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:id>/', recipe_details, name='recipe_detail'),
    path('recipe/<int:pk>/add_image/', add_image,name='add_image'),
    path('recipe/add', add_recipe, name ="add_recipe")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)