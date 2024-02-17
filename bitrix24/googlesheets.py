import httplib2
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheets:
    """Класс для авторизации на googleapis и добавления в таблицу google"""
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.SPREADSHEET_ID = settings.SPREADSHEET_ID
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("sac.json", self.SCOPES).authorize(
            httplib2.Http())

    def append_sheets(self, values: list, range_columns: str = "A:C") -> bool:
        try:
            service = build("sheets", "v4", http=self.creds)
            service.spreadsheets().values().append(
                spreadsheetId=self.SPREADSHEET_ID,
                range=range_columns,
                valueInputOption="RAW",
                body={"values": [values]},
            ).execute()
            return True

        except HttpError as error:
            print(f"Произошла ошибка: {error}")
            return False
