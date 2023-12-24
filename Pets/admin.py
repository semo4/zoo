from django.contrib import admin
from .models import Pet, Apply_adoption, Adoption_by_user

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ('petName', 'type', 'description')


class ApplyAdoptionAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'user_owner_id', 'approval_status')


class OfferAdoptionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'petName', 'breed')


admin.site.register(Pet, PetAdmin)
admin.site.register(Apply_adoption, ApplyAdoptionAdmin)
admin.site.register(Adoption_by_user, OfferAdoptionAdmin)
