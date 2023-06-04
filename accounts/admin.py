from django.contrib import admin
import sys
sys.path.append('/produto/')
sys.path.append('/empresa/')
from empresa.models import *
from produto.models import *
from accounts.models import *
admin.site.register(administrador)
admin.site.register(produtos)
admin.site.register(secao)
admin.site.register(preco)

admin.site.register(Tipos)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Empresa)

