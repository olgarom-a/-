# Ольга Ромашова, 23А когорта - дипломный проект
import stand_request
import data

def test_get_order_info_by_track():
    track = stand_request.post_order(data.creating_an_order).json()["track"]
    response = stand_request.get_order(track)
    assert response.status_code == 200




