from textblob import TextBlob
from newspaper import Article

if input("urls or file? ").lower().startswith("url"):

    urls = ['https://en.wikipedia.org/wiki/Computer_science',
        'https://store.steampowered.com/app/698780/Doki_Doki_Literature_Club/',
        'https://www.thetedkarchive.com/library/for-the-love-of-a-brother',
        'https://www.amnesty.org.uk/knowledge-hub/all-resources/china-1989-tiananmen-square-protests-demonstration-massacre/',
        'https://en.wikipedia.org/wiki/Hatred']

    for url in urls:
        article = Article(url)
        print(url)

        article.download()
        article.parse()
        article.nlp()

        text = article.text
        # print(text)

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        print(sentiment)

else:

    with open('emotions.txt', 'r') as f:
        text = f.read()

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        print(sentiment)
