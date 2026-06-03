class ExampleLibrary:
    """A simple Python keyword library for Robot Framework."""

    def create_greeting(self, greeting, name):
        return f"{greeting}, {name}!"

    def add_numbers(self, a, b):
        return int(a) + int(b)

    def filter_even_numbers(self, items):
        return [int(item) for item in items if int(item) % 2 == 0]
