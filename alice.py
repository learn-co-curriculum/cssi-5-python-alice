#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.


def GetUniqueWords(text):
  return 0  # Change me!


def main():
  # Open the file, read it into memory as a single string.
  with open('alice_in_wonderland.txt') as alice_file:
    alice_text = alice_file.read()

  print 'Unique words:', GetUniqueWords(alice_text)


if __name__ == '__main__':
  main()
