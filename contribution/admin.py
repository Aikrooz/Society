from django.contrib import admin

# Register your models here.

class ContributionAdmin(admin.ModelAdmin):
    list_display=('user','group','cycle_number','paid_at','status','verified_by')
    list_filter=('user','status',)