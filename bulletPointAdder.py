#! python3
import pyperclip
text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    if lines[i][0].isdecimal() or lines[i][0].isspace():
        continue
    else:
        lines[i] = '* '+ lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print('Processed text copied!!')
