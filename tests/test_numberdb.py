def test_number_add(client, app):
    assert client.get('/member/new').status_code == 200
    response = client.post(
        '/member/new', data={'name': 'testa', 'gender': '男',
                             'phone_number': 'testa',
                             'registration_date': '2020-01-01',
                             'birthday': '1995-01-01', 'belt': 'testa',
                             'gym': 'testa',
                             'unlimited_count': 1}
    )
    a = 'hh'
    assert a in response.data
