
def can_segment_str(s, dictionary):
    for i in range(len(s)):
        first_str = s[:i+1]
        second_str = s[i+1:]
        if first_str in dictionary:
            if not second_str or second_str in dictionary:
                return True
            else:
                return False

s = "datacamp"
dictionary = ["data", "camp", "cam", "lack"]
print(can_segment_str(s, dictionary))
