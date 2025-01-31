# using https://realpython.com/python-nltk-sentiment-analysis/ 

from nltk.stem.wordnet import WordNetLemmatizer

from nltk.corpus import twitter_samples, stopwords

from nltk.tag import pos_tag

from nltk.tokenize import word_tokenize

from nltk import FreqDist, classify, NaiveBayesClassifier
from sklearn.tree import DecisionTreeClassifier

import requests

from bs4 import BeautifulSoup

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier

sid = SentimentIntensityAnalyzer()



URL = "http://shakespeare.mit.edu/hamlet/full.html"

page = requests.get(URL)



soup = BeautifulSoup(page.content, "html5lib")

quotes = soup.findAll("blockquote")



alist = []

for quote in quotes:

 

  text = quote.get_text()

  #create new list var by splitting line by space

  text2 = text.split(' ')

  #create a new text dictionary

  text_dict = {}

  for i in range(0, len(text2), 2):

    #full the dict with the word and the term True

    text_dict[text2[i]] = True

  #pass the orginal text to a vader polarity scorer

  results = sid.polarity_scores(text)

  # Have postive quotes be marked as postive, and negative as negative

  if results['neg'] > results['pos']:

    

    alist.append((text_dict, "Negative"))

  else:

    alist.append((text_dict, "Positive"))





import re, string, random



def remove_noise(tweet_tokens, stop_words = ()):



  cleaned_tokens = []



  for token, tag in pos_tag(tweet_tokens):

    token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\

            '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)

    token = re.sub("(@[A-Za-z0-9_]+)","", token)



    if tag.startswith("NN"):

      pos = 'n'

    elif tag.startswith('VB'):

      pos = 'v'

    else:

      pos = 'a'



    lemmatizer = WordNetLemmatizer()

    token = lemmatizer.lemmatize(token, pos)



    if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:

      cleaned_tokens.append(token.lower())

  return cleaned_tokens



def get_all_words(cleaned_tokens_list):

  for tokens in cleaned_tokens_list:

    for token in tokens:

      yield token



def get_tweets_for_model(cleaned_tokens_list):

  for tweet_tokens in cleaned_tokens_list:

    yield dict([token, True] for token in tweet_tokens)



if __name__ == "__main__":



  positive_tweets = twitter_samples.strings('positive_tweets.json')

  negative_tweets = twitter_samples.strings('negative_tweets.json')

  text = twitter_samples.strings('tweets.20150430-223406.json')

  tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]



  stop_words = stopwords.words('english')



  positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

  negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')



  positive_cleaned_tokens_list = []

  negative_cleaned_tokens_list = []



  for tokens in positive_tweet_tokens:

    positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))



  for tokens in negative_tweet_tokens:

    negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))



  all_pos_words = get_all_words(positive_cleaned_tokens_list)



  freq_dist_pos = FreqDist(all_pos_words)

  print(freq_dist_pos.most_common(10))



  positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)

  negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)



  positive_dataset = [(tweet_dict, "Positive")

             for tweet_dict in positive_tokens_for_model]



  negative_dataset = [(tweet_dict, "Negative")

             for tweet_dict in negative_tokens_for_model]



  dataset = positive_dataset + negative_dataset



  random.shuffle(dataset)



  train_data = dataset[:7000]

  test_data = dataset[7000:]

  print(test_data[0])

  print(type(test_data[0]))

  print(type(test_data[0]))



  classifier = NaiveBayesClassifier.train(train_data)
  
  from sklearn.feature_extraction.text import TfidfTransformer
  from sklearn.feature_selection import SelectKBest, chi2
  from sklearn.naive_bayes import MultinomialNB
  from sklearn.pipeline import Pipeline
  pipeline = Pipeline([('tfidf', TfidfTransformer()),
                     ('chi2', SelectKBest(chi2, k=1000)),         
                     ('nb', MultinomialNB())])
  classif = SklearnClassifier(pipeline)
  


  


  print(classif)
  print("Accuracy is:", classify.accuracy(classifier, alist))



  print(classifier.show_most_informative_features(10))



  custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."



  custom_tokens = remove_noise(word_tokenize(custom_tweet))



  print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))

