from django.contrib import admin
from .models import (
    User, Login, Contact, Donar, Patient,
    BloodRequest, BloodDonation, Feedback,
    BloodStock, ContactFooter, ContactTeam
)

# =========================
# USER ADMIN
# =========================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'fullname',
        'email',
        'phone',
        'gender',
        'role',
        'created_at'
    )

    search_fields = ('fullname', 'email', 'phone', 'role')
    list_filter = ('role', 'gender')


# =========================
# BLOOD STOCK ADMIN
# =========================
@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):

    list_display = ('bloodgroup', 'units', 'bankname')
    list_editable = ('units',)
    search_fields = ('bloodgroup', 'bankname')


# =========================
# DONOR ADMIN (IMPORTANT UPDATE)
# =========================
@admin.register(Donar)
class DonarAdmin(admin.ModelAdmin):

    list_display = (
        'fullname',
        'bloodgroup',
        'units',
        'date',
        'status'
    )

    list_filter = ('status', 'bloodgroup', 'date')
    search_fields = ('fullname', 'email', 'contact')

    actions = ['approve_donations', 'reject_donations']

    def approve_donations(self, request, queryset):
        queryset.update(status='approved')

    def reject_donations(self, request, queryset):
        queryset.update(status='rejected')

    approve_donations.short_description = "Approve selected donations"
    reject_donations.short_description = "Reject selected donations"


# =========================
# SIMPLE REGISTRATIONS
# =========================
admin.site.register(Login)
admin.site.register(Contact)
admin.site.register(Patient)
admin.site.register(BloodRequest)
admin.site.register(BloodDonation)
admin.site.register(Feedback)
admin.site.register(ContactFooter)
admin.site.register(ContactTeam)


# from django.contrib import admin
# from .models import User, Login, Contact, Donar, Patient, BloodRequest, BloodDonation, Feedback, BloodStock,ContactFooter,ContactTeam

# # @admin.register(User)
# # class UserAdmin(admin.ModelAdmin):
# #     list_display = ('fullname', 'email', 'phone', 'gender', 'created_at')
# #     search_fields = ('fullname', 'email', 'phone')
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):

#     list_display = (
#         'fullname',
#         'email',
#         'phone',
#         'gender',
#         'role',
#         'created_at'
#     )

#     search_fields = (
#         'fullname',
#         'email',
#         'phone',
#         'role'
#     )

#     list_filter = ('role', 'gender')

# @admin.register(BloodStock)
# class BloodStockAdmin(admin.ModelAdmin):
#     list_display = ('bloodgroup', 'units', 'bankname')
#     list_editable = ('units',)

# admin.site.register(Login)
# admin.site.register(Contact)
# admin.site.register(Donar)
# admin.site.register(Patient)
# admin.site.register(BloodRequest)
# admin.site.register(BloodDonation)
# admin.site.register(Feedback)
# admin.site.register(ContactFooter)
# admin.site.register(ContactTeam)