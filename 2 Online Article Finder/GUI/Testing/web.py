from modules import *
import modules

def open_google(article_name):
    wb.open(f"www.google.com/search?q={article_name}")
if __name__ == '__main__':
    open_google()
