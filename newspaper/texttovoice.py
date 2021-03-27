from newspaper import Article
import nltk
from gtts import gTTS
import os
#getting the article from the link
article = Article('https://www.thedailystar.net/opinion/news/apparel-diplomacy-the-post-ldc-era-2055217')

article.download()
article.parse()
#applying natural language processing
nltk.download('punkt')
article.nlp()

#defining the variable to store the article
mytext = article.text
#language of speech
language = 'en'
#pass the text and language to the engine to convert the text to speech and store it in a variable
myobj = gTTS(text=mytext, lang=language, slow=False) 
#saVING THE speech to Mp3 file
myobj.save("read_article.mp3")
#speech
os.system("start read_article.mp3")

