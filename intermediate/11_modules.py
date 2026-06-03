# 11_modules.py
# Demonstrates module import, aliasing, and __name__ guard.

import math
import json as js

print('math.sqrt(16) =', math.sqrt(16))
print('json dump:', js.dumps({'a': 1, 'b': 2}))

if __name__ == '__main__':
    print('This module was run directly.')
else:
    print('This module was imported.')
