import modules
from modules import *

def getarticle(article_name):

    article = wiki.Wikipedia(
            language='en',
            user_agent="MyCustomUserAgent/1.0 (https://mywebsite.com)"
        )
    print("\n")
    site = article.page(article_name)
    if site.exists():
        print("There is a short article on this!")
        print("\n")
        print(f"\t\t\t\t{site.title}")
        print("\n")
        print(f"{site.summary[:]}")
    else:
        print("Article not found!")
        print("searching on google....")
        web.open_google(article_name=article_name)

if __name__ == '__main__':
    getarticle()