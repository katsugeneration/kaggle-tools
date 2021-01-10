from kaggle_tools.dummy_env import DummyEnv


def filter_func(x: list) -> list:
    return list(filter(lambda y: y != 2, x))


def map_func(x: list) -> list:
    return [y ** 2 for y in x]


class TestDummyEnv:
    def test_init(self):
        data = [1, 2, 3, 4]
        DummyEnv(data, filter_func, map_func, 2)

    def test_iter_test(self):
        data = [1, 2, 3, 4]
        env = DummyEnv(data, filter_func, map_func, 2)

        iter = env.iter_test()
        assert next(iter) == [1, 9]
        assert next(iter) == [16]
