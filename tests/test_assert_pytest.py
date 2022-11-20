def func(x):
    return x + 1


print("func(32):", func(32))


def test_answer():
    assert func(4) == 5
    assert func(3) == 5


def testanswer():
    assert func(4) == 5
    assert func(3) == 5


def answer_test():
    assert func(4) == 5
    assert func(3) == 5


class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
