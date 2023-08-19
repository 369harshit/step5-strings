def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_sentence = ' '.join(reversed_words)  # Join the words back into a sentence
    return reversed_sentence

sentence = "the sky is blue"
reversed_sentence = reverse_words(sentence)
print("Reversed Sentence:", reversed_sentence)
