#Широков Вячеслав 29 когорта

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.

import sender_stand_request

# Определение функции check_new_order для отправки GET-запроса для проверки заказа
def check_new_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH + str(track))
    return response.status_code

# Тест test_status_code для проверки, что по треку заказа можно получить данные о заказе
def test_new_order_check_status_code():
     # Проверяем что код ответа 200
     assert check_new_order(current_track) == 200
