from PANDEM import *
from newsapi import NewsApiClient

class  NewsApiThread(QtCore.QThread):
    NewsSignal = QtCore.pyqtSignal(list)
    def __init__(self, parent=None):
        super(NewsApiThread, self).__init__(parent=parent)
        self.newsapi = NewsApiClient(api_key='fd2bf691ef6845e1b7bb0bf33d816c45')


    def run(self):
        while True:
            data = self.newsapi.get_top_headlines(language = 'en',category='technology')
            headlines = data['articles']
            length = len(headlines)
            articles = []
            for x in range(length):
                #articles[x] = headlines[x]['title']
                articles.append(headlines[x]['title'])

            self.NewsSignal.emit(articles)
            QtCore.QThread.sleep(5*60)
