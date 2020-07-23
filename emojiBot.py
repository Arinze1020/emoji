#import emoji
import emoji

print(emoji.emojize(':thumbs up:'))
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.demojize('Python is 👍'))