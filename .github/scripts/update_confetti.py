import os
import datetime
import pytz

# Set your timezone (Nairobi, UTC+3)
YOUR_TIMEZONE = pytz.timezone('Africa/Nairobi')
BIRTHDAY = '07-12'  # July 12
CONFETTI_URL = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnhtajZpZnd6eWdlM2V4bmlxejYxejV0MWI3NnJ1MG53MnNjaHc3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8AdhxLETq6WhyyyxBk/giphy.gif"

try:
    # Get current time in your timezone
    now = datetime.datetime.now(YOUR_TIMEZONE)
    today = now.strftime('%m-%d')
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    confetti_html = f'<div align="center"><img src="{CONFETTI_URL}" width="100%"></div>\n\n'
    
    if today == BIRTHDAY:
        print("🎉 Happy Birthday! Adding confetti")
        if '<!-- BIRTHDAY_CONFETTI -->' in content:
            new_content = content.replace('<!-- BIRTHDAY_CONFETTI -->', confetti_html)
        else:
            new_content = confetti_html + content
    else:
        print("Not birthday - removing confetti")
        new_content = content.replace(confetti_html, '<!-- BIRTHDAY_CONFETTI -->')
    
    with open('README.md', 'w') as f:
        f.write(new_content)

except Exception as e:
    print(f"Error updating confetti: {e}")
    exit(1)
