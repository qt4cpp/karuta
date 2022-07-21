from src.cardcontroller import CardController


def test_read():
    controller = CardController('test_4letters.csv')

    controller.read()
    first_line = controller.pick(0)
    assert first_line[0] == '四字熟語'
    assert first_line[1] == 'よじじゅくご'


def test_pick():
    assert False
