from django.urls import path
from . import views

urlpatterns = [ 
    
                path('diamondberry/',views.index, name='home'),
                path('diamondberry/<int:article_id>/',views.article_page, name='article'),
                path('components/', views.components, )
                
                ]       
