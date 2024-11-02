from c import logger_decorator


class TestObject:
    def __init__(self, number):
        self.a = number
    @logger_decorator
    def test_member_function(self, **kwargs):
        return kwargs.get('a') * 2

@logger_decorator
def test_function(**kwargs):
    return kwargs.get('a') * 2

TestInstance = TestObject(3);
print(TestInstance.test_member_function(a = 3))

# print(test_function(a = 2))
#