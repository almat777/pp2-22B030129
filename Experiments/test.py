import fileinput
import re
fn = "transactions.txt"
for line in fileinput.input(fn, inplace=True):
    new_line = re.sub('(\d{2}|[a-yA-Y]{3})\/(\d{2})\/(\d{2, 4})', r'\1-\2-\3', line)
    print(new_line)