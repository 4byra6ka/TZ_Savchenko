import requests
from django.conf import settings


def crm_deal_get(deal_id: str) -> tuple[str, str]:
    """Получение данных сделки с Bitrix24"""
    params = {'id': deal_id}
    response = requests.post(settings.URL_CRM_DEAL_GET, params=params)
    data = response.json()
    return data['result']['CONTACT_ID'], data['result']['COMMENTS']


def crm_contact_get(contact_id: str) -> tuple[str, str]:
    """Получение данных контакта с Bitrix24"""
    phones = ""
    params = {'id': contact_id}
    response = requests.post(settings.URL_CRM_CONTACT_GET, params=params)
    data = response.json()
    for phone in data['result']['PHONE']:
        phones += f'{phone['VALUE']} '
    return f"{data['result']['NAME']} {data['result']['LAST_NAME']}", phones
