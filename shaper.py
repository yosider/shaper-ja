import pyperclip

txt = pyperclip.paste()
txt = txt.replace(' ', '')
txt = txt.replace('\r', '')
txt = txt.replace('\n', '')

pyperclip.copy(txt)
# print(txt)
