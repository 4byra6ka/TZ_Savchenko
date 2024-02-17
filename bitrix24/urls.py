from django.urls import path

from bitrix24.apps import Bitrix24Config
from bitrix24.views import on_crm_deal_add

app_name = Bitrix24Config.name

urlpatterns = [
    path("oncrmdealadd/", on_crm_deal_add),
]
