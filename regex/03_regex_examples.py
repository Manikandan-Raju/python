# 03_regex_examples.py
# Common regex usage examples for interview practice.

import re

text = 'Contact: alice@example.com or bob@example.org.'
email_pattern = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
print('Emails:', email_pattern.findall(text))

mobile_text = 'Call me at +1-555-123-4567 or 555.234.5678.'
phone_pattern = re.compile(r'\+?\d[\d.\- ]{7,}\d')
print('Phone numbers:', phone_pattern.findall(mobile_text))

word_boundary = re.compile(r'\bcat\b')
print('Matches cat as a whole word:', word_boundary.findall('cat scatter category'))

whitespace = re.compile(r'\s+')
print('Normalized:', whitespace.sub(' ', 'Hello\tworld\nnew line'))
