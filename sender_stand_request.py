# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

# Запрос на получение заказа по номеру
def get_info_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH + str(track_id))


