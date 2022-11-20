class UnexpectedType(Exception):
    pass


class TestClassDemoInstanceBis:
    value = 0.0
    value_bis = 0.0

    def test_function(self):
        self.value = 1
        assert self.value == 1
        if not (isinstance(self.value, type(self.value_bis))):
            raise UnexpectedType
