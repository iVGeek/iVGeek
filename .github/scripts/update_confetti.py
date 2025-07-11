import os
import datetime

BIRTHDAY = os.getenv('BIRTHDAY', '01-01')
TODAY = datetime.datetime.now().strftime('%m-%d')
CONFETTI_URL = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3d1am5jeW1xM2Q0c2p0YjM4eXJ6b3RlZzQ1dW5uN3l4dTZ3bDd6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/3o7abKhOpu0NwenH3O/giphy.gif"

with open('README.md', 'r') as f:
    content = f.read()

confetti_html = f'<div align="center"><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnhtajZpZnd6eWdlM2V4bmlxejYxejV0MWI3NnJ1MG53MnNjaHc3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8AdhxLETq6WhyyyxBk/giphy.gif" width="100%"></div>\n\n'

if TODAY == BIRTHDAY:
    if '<!-- BIRTHDAY_CONFETTI -->' in content:
        new_content = content.replace('<!-- BIRTHDAY_CONFETTI -->', confetti_html)
    else:
        new_content = confetti_html + content
else:
    new_content = content.replace(confetti_html, '<!-- BIRTHDAY_CONFETTI -->')

with open('README.md', 'w') as f:
    f.write(new_content)
