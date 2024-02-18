# <img src="https://www.bitrix24.ru/favicon.svg" width="89"/> <img src="https://cdn-icons-png.flaticon.com/512/5968/5968557.png" width="89"/> <img src="https://www.svgrepo.com/show/303231/docker-logo.svg" width="89"/> 
## Итеграцию между приложениями Битрикс24 и Google таблицы"

***
#### Реализованы задачи:
* принимает информацию с Битрикса о созданной сделке;
* записывает данные в БД;
* записывает данные в гугл таблицы;
***



### Прежде чем начать использовать проект нужно:
* Для интеграции с Bitrix24 нужно:
  * создать исходящий webhook и записать `Токен приложения` в `.env API_WEBHOOK_BITRIX24`
  * создать входящий webhook для запроса сделок `crm.deal.get` и записать `URL` в `.env URL_CRM_DEAL_GET`
  * создать входящий webhook для запроса сделок `crm.contact.get` и записать `URL` в `.env URL_CRM_CONTACT_GET`
* Для интеграции с Google Sheets нужно:
  * [создать сервисный аккаунт](https://support.google.com/a/answer/7378726?hl=ru) по инструкции. При выборе библиотеки добавить `Google Sheets API`. 
  * После выполнения инструкции сохраненный ключ в формате `json` переименовать в `sac.json` и положить в корень с клонированного репозитория.
  * Создать Google Sheets документ и назначить права доступа на редактирования сервисному аккаунту Google который был создан ранее.
  * В открытом документе Google Sheets браузера скопировать нужный фрамент URL для заполнения ключа `.env SPREADSHEET_ID`. <br> `https://docs.google.com/spreadsheets/d/<Ключ SPREADSHEET_ID>/edit#gid=0`
* Создать файл `.env` для переменного окружения.

### `.env`
    API_WEBHOOK_BITRIX24=#API Ключ на исходящий webhook Bitrix 24
    URL_CRM_DEAL_GET=#URL сделок для входящего webhook Bitrix 24
    URL_CRM_CONTACT_GET=#URL сделок для входящего webhook Bitrix 24
    SPREADSHEET_ID=#ID таблицы из GOOGLE SHEETS

***
### Запуск Docker Compose проекта
    git cline https://github.com/4byra6ka/TZ_Savchenko.git
    cd TZ_Savchenko
    vi .env
    docker-compose build
    docker-compose up
***

