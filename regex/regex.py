import re

def get_struct(header):
    search = re.search(r'struct[\s\t\n]+(\w+)[\s\t\n]+{',header)
    return search
