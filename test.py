#Широков Вячеслав 29 когорта

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.

import sender_stand_request

def test_positive_assert_order_creation():
    new_response = sender_stand_request.post_new_order()
    track_id = new_response.json()['track']
    response = sender_stand_request.get_info_track(track_id)
    assert response.status_code == 200
