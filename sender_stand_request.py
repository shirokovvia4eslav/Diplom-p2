# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового закааз
def create_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)
    return response.json()["track"]

# Переменная для хранения нового заказа
current_track = create_new_order()

# Определение функции check_new_order для отправки GET-запроса для проверки заказа
def check_new_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH + str(track))
    return response.status_code

# Тест test_status_code для проверки, что по треку заказа можно получить данные о заказе
def test_new_order_check_status_code():
     # Проверяем что код ответа 200
     assert check_new_order(current_track) == 200