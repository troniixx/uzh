def text_analysis(text):
    word_count = 0
    longest_word = ""
    
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word
        
        word_count += 1
        
    return word_count, longest_word

input_text = "This is a simple NLP-related exercise for debugging. Correct the code."
word_count, longest_word = text_analysis(input_text)

print(f"Word count: {word_count}")
print(f"Longest word count: {longest_word}")