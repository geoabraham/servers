from servers import dummy


def test_dummy():
    assert dummy.func(2) == 1
