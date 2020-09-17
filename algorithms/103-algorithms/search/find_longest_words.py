text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus ipsum et facilisis dignissim. Duis mattis enim urna. Quisque orci nunc, vulputate id accumsan nec, imperdiet sit amet sem. Integer consequat nibh vel mattis elementum. Nam est elit, sodales vitae augue nec, consequat porttitor nibh. Aliquam ut risus vehicula, egestas ligula sed, egestas neque. Fusce hendrerit vel risus in molestie. Morbi molestie eleifend odio vel ullamcorper. Donec at odio libero. Quisque vulputate nisl nisi, ut convallis lorem vulputate et. Aenean pretium eu tellus a dapibus. Ut id sem vulputate, finibus erat quis, vestibulum enim. Donec commodo dui eros, non hendrerit orci faucibus eu. Integer at blandit ex. Duis posuere, leo non porta tincidunt, augue turpis posuere odio, sed faucibus erat elit vel turpis. Quisque vitae tristique leo."""

import re

words = text.split()
processed_words = [re.sub("[^A-Za-z]+", "", word) for word in words]
print(processed_words)

longest_word = max(processed_words, key=len)
print("The longest word: {}".format(longest_word))

n = len(longest_word)
longest_words = [word for word in processed_words if len(word) == n]
print("The longest words: {}".format(longest_words))