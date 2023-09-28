s = input()
sub_string = 'EGYPT'

if sub_string in s:
    s = s.replace(sub_string, ' ')
print(s)
