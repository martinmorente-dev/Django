#Importamos nuestras funciones del views
from django.urls import path
from .views import list_index,update,delete

urlpatterns =[
#Url Lista (Lectura+Escritura)
path('',list_index, name='list.view'),
#Url Actualizar
path('list-upd/<l_id>',update,name='list.update'),
#Url Borrar
path('list-del/<l_id>',delete,name='list.delete')
]
