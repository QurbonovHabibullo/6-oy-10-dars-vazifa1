from django.urls import path
from .views import (turlar_list, gullar_list,
                tur_by_gullar,gul_detail,add_tur,add_gul,update_tur,update_gul,delete_tur,delete_gul)

urlpatterns = [
    path('', turlar_list, name='turlar_list'),
    path('gullar/', gullar_list, name='gullar_list'),
    path('turlar/<int:tur_id>/', tur_by_gullar, name='tur_by_gullar'),  
    path('gul/<int:gul_id>/',gul_detail,name="gul_detail"),
    path('add_tur/',add_tur,name="add_tur"),
    path('add_gul/',add_gul,name="add_gul"),
    path('update_tur/<int:tur_id>/', update_tur, name='update_tur'), 
    path('update_gul/<int:gul_id>/', update_gul, name='update_gul'), 
    path('delete_tur/<int:tur_id>/',delete_gul,name="delete_gul"),
    path('delete_gul/<int:gul_id>/',delete_gul,name="delete_gul"),
    
]

