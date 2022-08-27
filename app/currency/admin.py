from django.contrib import admin
from currency.models import Rate, Source, ContactUs

from rangefilter.filters import DateTimeRangeFilter


class RateAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'base_currency_type',
                    'currency_type',
                    'sale',
                    'buy',)
    readonly_fields = ('sale', 'buy',)
    search_fields = ("base_currency_type",
                     'currency_type',
                     'sale',
                     'buy'
                     )

    list_filter = ('base_currency_type',
                   ('created', DateTimeRangeFilter),
                   )

    def has_delete_permission(self, request, obj=None):
        return False


class SourceAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'source_url',
                    'name')


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email_from',
                    'email_to',
                    'subject',
                    'message')
    search_fields = (
        "id",
        "email_from",
        "email_to",
        "subject",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
