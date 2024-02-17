from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bitrix24.googlesheets import GoogleSheets
from bitrix24.serializers import Bitrix24Serializer
from bitrix24.services import crm_deal_get, crm_contact_get


@api_view(['POST'])
def on_crm_deal_add(request, *args, **kwargs):
    """Обработка запроса в Webhook Bitrix24 """
    try:
        if request.method == 'POST' and request.data['auth[application_token]'] == settings.API_WEBHOOK_BITRIX24:
            contact_id, comments = crm_deal_get(request.data['data[FIELDS][ID]'])
            full_name, phones = crm_contact_get(contact_id)

            serializer = Bitrix24Serializer(data={
                'full_name': full_name,
                'phone': phones,
                'comment': comments,
            })
            if serializer.is_valid():
                serializer.save()
                gs = GoogleSheets()
                gs.append_sheets([full_name, phones, comments])
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except KeyError as error:
        print(f"Произошла ошибка: {error}")
        return Response(status=status.HTTP_400_BAD_REQUEST)
