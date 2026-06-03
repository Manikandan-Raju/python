# 10_context_manager.py
# Demonstrates the with-statement and writing a custom context manager.

# Built-in context manager with open():
with open('example.txt', 'w') as f:
    f.write('Hello from context manager')

print('Wrote example.txt')

# Custom context manager using class methods:
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        self.end = time.time()
        print('Elapsed:', self.end - self.start)
        return False

with Timer() as timer:
    total = sum(range(1000000))
    print('Sum computed:', total)
