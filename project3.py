'''
Project 3 - Reading Ease - Fall 2024  
Author: Arnav Gupta 906708722

Analyzes a txt file and calculates various statistics, including reading ease score and grade level. 
Also allows users to check the frequency of specific words in the text.

I have neither given or received unauthorized assistance on this assignment.
Signed: Arnav Gupta
'''


def read_text(filename):
    """
    Reads the txt file and returns a single string

    Args:
        filename (str): The name of the  file to read

    Returns:
        str: The contents of the text file
    """
    with open(filename, 'r') as file:
        return file.read()


def clean_text(text):
    """
    Cleans a string by converting it to lowercase and removing punctuatio

    Args:
        text (str): The text to clean

    Returns:
        str: The cleaned text
    """
    punctuation = ",:;?![]*()-'\"`."
    cleaned_text = text.lower()
    for char in punctuation:
        cleaned_text = cleaned_text.replace(char, '')
    return cleaned_text


def get_word_frequencies(words):
  """
  Calculates the frequency of each word in the list

  Args:
    words (list): A list of words from the cleaned text

  Returns:
    dict: A dictionary where keys are words and values are their frequencies
  """

  frequencies = {}
  for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1
  return frequencies

def count_syllables(word):
    """ Returns the number of syllables in the specified word

    Args:
        word (str): The word to analyze

    Returns:
        int: The estimated number of syllables in the word
    """
    syllables = 0
    vowels = 'aeiouy' ##y in certain cases ???
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            syllables += 1
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le'): #If word is "table", the condition word.endswith('le') is true cuz "table" ends with "le". 
        syllables += 1
    if syllables == 0:
        syllables = 1
    return syllables


def count_all_syllables(words):
    """
    Calculates the total no. of syllables in a list of words.

    Args:
        words (list): A list of words from the cleaned text.

    Returns:
        as an int: The total number of syllables in all words.
    """
    
    total_syllables = 0
    for word in words:
        total_syllables += count_syllables(word)
    return total_syllables



def main():
  """
  The main program that reads a file, analyzes the text, and allows user interaction.
  """

  print("Welcome to the Reading Ease Analyzer!")
  filename = input("Name of file to analyze? ")
  text = read_text(filename)

  cleaned_text = clean_text(text)
  words = cleaned_text.split()

  num_sentences = text.count(".") + text.count("?") + text.count("!")
  num_words = len(words)
  num_unique_words = len(get_word_frequencies(words))
  avg_words_per_sentence = round(num_words / num_sentences, 1) if num_sentences > 0 else 0
  avg_syllables_per_word = round(count_all_syllables(words) / num_words, 1) if num_words > 0 else 0

  flesch_reading_ease = round(206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word), 1)
  import math
  us_grade_level = math.ceil(0.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59)
  us_grade_level = f"{us_grade_level:.1f}"


  # Prints stats
  print("Number of sentences:", num_sentences)
  print("Number of words:", num_words)
  print("Number of unique words:", num_unique_words)
  print("Average words per sentence:", avg_words_per_sentence)
  print("Average syllables per word:", avg_syllables_per_word)
  print("Flesch-Kincaid reading-ease score:", flesch_reading_ease)
  print("U.S. grade level:", us_grade_level)
  print()

  # Checks word frequencies
  while True:
    check_word = input("Enter word to check (\"q\" to quit): ").lower()
    if check_word == "q":
      break

    frequencies = get_word_frequencies(words)
    if check_word in frequencies:
      count = frequencies[check_word]
      print("The word \"" + check_word + "\" appears", count, ("times" if count > 1 else "time") + ".")
    else:
      print("The word \"" + check_word + "\" does not appear in the text.")
  
if __name__ == '__main__':
    main()