from django.contrib import admin

from .models import Atendimento, Pet, Tutor

admin.site.register(Tutor)
admin.site.register(Pet)
admin.site.register(Atendimento)
