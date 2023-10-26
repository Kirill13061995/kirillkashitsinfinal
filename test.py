import sender_stand_requests

# Кашицын Кирилл 9-я когорта, Дипломный проект, Инженер по тестированию плюс
# Проверка номера заказа
def nomer_zakaza():
    new_nomer_zakaza = sender_stand_requests.post_new_order()
    return new_nomer_zakaza.json()["track"]

 # Проверка, что код 200
def test_cod_otveta():
    c_track = nomer_zakaza()
    act_cod = sender_stand_requests.get_track(c_track).status_code
    assert act_cod == 200