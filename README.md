# telegram-brazzers-bot

This project is (hopefully) a Telegram bot that gets DMs. This bot should be a bot to which you can send an image and it sends you that image back but with a Brazzers watermark.

---
#### TODO LIST/ROADWAY:
- [ ] Create the bot implementation in Python, where it takes a file in as an output and returns an output file, with the Brazzers logo as a watermark in the bottom right corner
- [ ] Give the bot API access, probably using something such as Telegram or others, where it can be freely messaged and sent images to send back
- [ ] Publish the bot!

---
# Dev Things
The bot has all images it can add as a watermark in the 'watermarks' folder, all named by what they are (e.g. Brazzers logo = brazzers.png). They are saved as .png to allow alpha channel if necessary (or deemed so in development).

As a starter/reference image, I am using an image of polar bears, because they are cute.