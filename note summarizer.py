import nltk
import heapq

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text, num_sentences=3):
    # Tokenizing sentences
    sentences = sent_tokenize(text)
    
    # Tokenizing words
    words = word_tokenize(text.lower())
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    
    # Word frequency
    freq_table = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            freq_table[word] = freq_table.get(word, 0) + 1
    
    # Sentence scoring
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_table[word]
    
    # Selecting top sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Final summary
    summary = ' '.join(summary_sentences)
    
    return summary


#  User Input
text = input("Enter your notes:\n")

#  Get summary
summary = summarize_text(text, 3)

print("\n Summary:\n")
print(summary)
