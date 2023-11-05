import telebot
import time
import requests

# Enter your bot token here
bot_token = "6736736711:AAHX0hq_TFN8yUjfT2VTWcjOBgOmC-VH5FE"

# Enter your channel username or ID here
channel_id = "@Mehdicigarette"

# Function to send a picture from a URL to the channel
def send_picture():
    # Replace "picture_url" with the actual URL of your picture
    picture_url = "https://imageupload.io/ib/DRaxHSk2GCzWDgT_1699207640.jpg"
    response = requests.get(picture_url)
    if response.status_code == 200:
        with open("picture.jpg", "wb") as file:
            file.write(response.content)
        with open("picture.jpg", "rb") as picture:
            bot.send_photo(channel_id, picture)
    else:
        print("Failed to fetch the picture")

# Initialize the bot
bot = telebot.TeleBot(bot_token)

# Main loop to send a picture every minute
while True:
    send_picture()
    time.sleep(60)  # Wait for 60 seconds