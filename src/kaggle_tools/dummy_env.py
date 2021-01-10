# Kaggle dummy env with iteration test data getter
from typing import Callable, TypeVar, Iterable

T = TypeVar("T", bound=Iterable)


class DummyEnv:
    def __init__(
        self,
        test_data: T,
        filter_func: Callable[[T], T],
        map_func: Callable[[T], T],
        batch_num: int,
    ) -> None:
        self.test_data = test_data
        self.filter_func = filter_func
        self.map_func = map_func
        self.batch_num = batch_num

    def iter_test(self):
        data = self.filter_func(self.test_data)
        for i in range(0, len(data) // self.batch_num + 1):
            yield self.map_func(data)[
                self.batch_num * i : self.batch_num * (i + 1)  # noqa: E203
            ]
