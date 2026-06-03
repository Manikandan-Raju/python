import re

# Compile a pattern once and use it multiple times.
# This is useful when the same regular expression is applied to many strings.
STRUCT_PATTERN = re.compile(r'struct[\s\t\n]+(\w+)[\s\t\n]+{')
IDENTIFIER_PATTERN = re.compile(r'\b[a-zA-Z_]\w*\b')
EMAIL_PATTERN = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
WHITESPACE_PATTERN = re.compile(r'\s+')
CSV_SPLIT_PATTERN = re.compile(r'\s*,\s*')


def get_struct(header):
    """Return the struct name from a C-style struct declaration header."""
    return STRUCT_PATTERN.search(header)


def find_identifiers(code):
    """Return a list of identifier-like tokens from the given text."""
    return IDENTIFIER_PATTERN.findall(code)


def find_email_addresses(text):
    """Return all email-like substrings found in the text."""
    return EMAIL_PATTERN.findall(text)


def normalize_whitespace(text):
    """Replace runs of whitespace with a single space."""
    return WHITESPACE_PATTERN.sub(' ', text).strip()


def split_csv(line):
    """Split a comma-separated line while ignoring spaces around commas."""
    return CSV_SPLIT_PATTERN.split(line)


if __name__ == '__main__':
    sample_header = 'struct MyType {\n    int x;\n}'
    print('struct match:', get_struct(sample_header).group(1))

    sample_code = 'int main() { int _value = 42; }'
    print('identifiers:', find_identifiers(sample_code))

    sample_text = 'contact: alice@example.com, bob@example.org'
    print('emails:', find_email_addresses(sample_text))

    messy = 'This   text\tcontains\nmultiple   spaces.'
    print('normalized:', normalize_whitespace(messy))

    csv_line = 'apple, banana , cherry ,date'
    print('csv fields:', split_csv(csv_line))
