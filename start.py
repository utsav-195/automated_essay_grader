import nltk
import statistics
import autocorrect
from spellchecker import SpellChecker

essay = "Tokenizer's divide strings int lists of substrings. For exaple, divide strings"


# returns list of misspelled words, corrected errors and the total number of misspelled words
def typos(words):
    spell = SpellChecker()

    # find those words that may be misspelled
    misspelled = spell.unknown(words)
    corrected_words = {}
    for word in misspelled:
        # Get the one `most likely` answer
        correct_spell = spell.correction(word)
        if correct_spell != word:
            corrected_words[word] = correct_spell

    misspelled = [word for word in corrected_words]
    corrected_words = [corrected_words[word] for word in corrected_words]
    return misspelled, corrected_words, len(misspelled)


# returns the list of stop words
def get_stop_words():
    stop_words = nltk.corpus.stopwords.words('english')
    return stop_words


# returns all sentences and total number of sentences
def tokenize_sentences(data):
    sent_token = nltk.tokenize.sent_tokenize(data)
    return sent_token, len(sent_token)


# returns all tokens, all types and total number of tokens
# if punc is False(default True), then punctuations are not removed
# If lower is False(default True), then words are not kept as is, not converted to lower case
def tokenize_words(data, punc=True, remove_stop_words=False, lower=True):
    if lower:
        word_tokens = nltk.tokenize.word_tokenize(data.lower())
    else:
        word_tokens = nltk.tokenize.word_tokenize(data)
    if punc:
        word_tokens = [word for word in word_tokens if len(word) > 1]
    if remove_stop_words:
        stop_words = get_stop_words()
        word_tokens = [word for word in word_tokens if word not in stop_words]

    return word_tokens, list(set(word_tokens)), len(word_tokens)


# returns frequency of each word
def token_frequency(words):
    frequency_of_tokens = nltk.FreqDist(words)
    return frequency_of_tokens


# returns length of each word in token
def token_length(words):
    len_of_tokens = {}
    for word in words:
        len_of_tokens[word] = len(word)
    return len_of_tokens


# returns length of sentences in terms of number of words and the average length of sentences
def sentence_length(sent):
    len_of_sent = []
    for s in sent:
        len_of_sent.append(tokenize_words(s)[1])
    return len_of_sent, statistics.mean(len_of_sent)


def syntactic_correctness(sent):
    print(sent)
    rd_parser = nltk.RecursiveDescentParser(sent)
    print(rd_parser)
    for tree in rd_parser:
        print(tree)


# syntactic_correctness(tokenize_sentences(essay)[0][0])
print(tokenize_words(essay))
