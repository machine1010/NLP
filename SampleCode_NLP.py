################### Word tokenization
#Tokenization is a very common task in NLP, it is basically a task of chopping a character into pieces, called as token.
from spacy.lang.en import English
nlp = English()

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)
print(my_doc)
# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)
print(token_list[:5])
#######################
