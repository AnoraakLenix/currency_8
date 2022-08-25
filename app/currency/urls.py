from django.contrib import admin
from django.urls import path, include
# from currency.views import rate_list, contact_list, rate_create, rate_update, rate_details, \
#     rate_delete, source_update, source_delete, source_details, source_create, source_list
from currency import views

app_name = 'currency'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view()),

    path('source/list/', views.SourceListView.as_view(), name='source_list'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/details/<int:pk>/', views.SourceDetailsView.as_view(), name='source_details'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),

    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailsView.as_view(), name='rate_details'),

    path('__debug__/', include('debug_toolbar.urls'))

]
