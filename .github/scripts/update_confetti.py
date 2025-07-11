import os
import datetime
import pytz

# Configuration
YOUR_TIMEZONE = pytz.timezone('Africa/Nairobi')  # Nairobi time
BIRTHDAY_MONTH = 7  # July
BIRTHDAY_DAY = 12   # 12th
CONFETTI_URL = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnhtajZpZnd6eWdlM2V4bmlxejYxejV0MWI3NnJ1MG53MnNjaHc3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8AdhxLETq6WhyyyxBk/giphy.gif"

try:
    # Get current time in Nairobi
    now = datetime.datetime.now(YOUR_TIMEZONE)
    
    # Check if today is July 12th
    is_birthday = now.month == BIRTHDAY_MONTH and now.day == BIRTHDAY_DAY
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    confetti_html = f'<div align="center"><img src="{CONFETTI_URL}" width="100%"></div>\n\n'
    
    if is_birthday:
        print("🎉 Happy Birthday! Adding confetti")
        if '<!-- BIRTHDAY_CONFETTI -->' in content:
            new_content = content.replace('<!-- BIRTHDAY_CONFETTI -->', confetti_html)
        else:
            new_content = confetti_html + content
    else:
        print("Not birthday - removing confetti")
        # Remove confetti if exists
        new_content = content.replace(confetti_html, '<!-- BIRTHDAY_CONFETTI -->')
        # Ensure placeholder is present
        if '<!-- BIRTHDAY_CONFETTI -->' not in new_content:
            new_content = '<!-- BIRTHDAY_CONFETTI -->\n\n' + new_content
    
    with open('README.md', 'w') as f:
        f.write(new_content)

except Exception as e:
    print(f"Error updating confetti: {e}")
    exit(1)
