
from django.contrib import admin
from django.urls import path
from currency.views import rate_list, contact_list, index, http_response, rate_create, rate_update, rate_details, \
    rate_delete, source_update, source_delete, source_details, source_create, source_list


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('contactus/list/', contact_list),
    path('response/', http_response),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:source_id>/', source_update),
    path('source/details/<int:source_id>/', source_details),
    path('source/delete/<int:source_id>/', source_delete),



]
