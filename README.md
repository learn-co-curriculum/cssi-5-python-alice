---
tags: kids, python, alice, analyzing text
languages: python
level: 2
type: lab
---
##ALICE IN WONDERLAND

###Text Analyzing App:
<img src="http://www.alice-in-wonderland.net/alicepic/alice-in-wonderland/1book33.jpg" width="200px" align="right" hspace="10">
Using the code snippet in `alice.py` as a starting point, analyze the text of Alice in Wonderland, in `alice.txt`, to determine how many unique words are in the book.

You will need to fill in the `GetUniqueWords()` function with your own logic.

Once you have that working, extend the code to do more analysis. Each bit of analysis should go in its own function. Be on the look out for code you can share between functions; move that code into helper functions.

What are the top 10 most frequently-used words in the text?
What are the 10 least frequently-used words in the text?
How many words are used more than 100 times? What are they?
How many times does the word "Alice" appear? How about "Wonderland"?
What are the top 10 most frequently-used bigrams (pairs of consecutive words) in the text? For example "use the big spoon" would generate three bigrams: "use the", "the big" and "big spoon".

###Challenge:
Using the frequency data collected above and Python's random module, generate random text with the same frequency distribution as Alice in Wonderland. That is, if a word appears 5% of the time in Alice in Wonderland, it should appear 5% of the time in your randomly-generated book.

###Even More Challenge:
Make the text as realistic as possible. The output from the first challenge will be random, but it will likely look like nonsense: the punctuation will be wrong, the sentence structure will be weird, etc. Using the analysis techniques above and any others you come up with, try to make the randomly generated text as realistic as possible.
