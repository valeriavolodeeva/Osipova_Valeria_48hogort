import sender_stand_request
# Валерия Осипова, 48-я когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order_by_track():
    create_response = sender_stand_request.create_order()

    assert create_response.status_code == 201, (
        f"Не удалось создать заказ: {create_response.status_code}, "
        f"{create_response.text}"
    )

    response_body = create_response.json()

    assert "track" in response_body, (
        f"В ответе создания заказа нет поля 'track': {response_body}"
    )

    track = response_body["track"]
    assert track, "Трек-номер заказа пустой"

    get_response = sender_stand_request.get_order(track)

    assert get_response.status_code == 200, (
        f"Ожидался код 200, получен {get_response.status_code}. "
        f"Ответ: {get_response.text}"
    )

    get_response_body = get_response.json()

    assert "order" in get_response_body, (
        f"В ответе отсутствует объект 'order': {get_response_body}"
    )
