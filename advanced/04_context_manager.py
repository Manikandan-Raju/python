# 04_context_manager.py
# Advanced context manager examples with generator-based contextlib and custom classes.

from contextlib import contextmanager


@contextmanager
def open_file(path, mode='r'):
    file = open(path, mode)
    try:
        yield file
    finally:
        file.close()


with open_file('advanced_example.txt', 'w') as f:
    f.write('Advanced context manager example')


# Custom context manager class with resource handling

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        self.end = time.time()
        print('Elapsed time:', self.end - self.start)
        return False


with Timer():
    total = sum(range(1000000))
    print('Total:', total)
