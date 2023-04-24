from django.contrib import admin
import sys
sys.path.append('/produto/')
from produto.models import *
from accounts.models import *
admin.site.register(administrador)
admin.site.register(produtos)
admin.site.register(secao)
admin.site.register(preco)
