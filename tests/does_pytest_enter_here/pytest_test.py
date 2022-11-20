def func(x):
    return x + 1


print("func(32):", func(32))


def test_answer_bis():
    assert func(4) == 5
    assert func(3) == 5
