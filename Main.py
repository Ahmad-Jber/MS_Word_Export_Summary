from Summarizer import nltk_summarizer
from word_doc import add_content

text_file = open("input_file.txt", "r")
data = text_file.read()
text_file.close()

output_file = open("output_file.txt", "w+")
output_file.write(nltk_summarizer(data))

title = input("Enter Title:\t")
add_content(title, nltk_summarizer(data))
