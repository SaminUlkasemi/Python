import pprint

message = "What will eventually happen to the universe? The question \
must have occurred in one form or another to speculative \
minds since time immemorial. The question may take the form \
of asking what is the ultimate fate of the Earth and of mankind. \
It is only in the last two or three decades that enough progress \
has been achieved in astronomy and cosmology (the study of \
the universe as a whole) for one to be able to give at least \
plausible answers to this kind of question"

count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1


pprint.pprint(count)
print("obtain the prettified text as a string value instead of displaying it on the screen")
print(pprint.pformat(count))