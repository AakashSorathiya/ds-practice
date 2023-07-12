import requests
from html.parser import HTMLParser
from nlp_rake import Rake
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class MyHTMLParser(HTMLParser):
    script = False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script", "style"]:
            self.script = True
    def handle_endtag(self, tag):
        if tag.lower() in ["script", "style"]:
            self.script = False
    def handle_data(self, data):
        if str.strip(data)=="" or self.script:
            return
        # print(data)
        self.res += ' '+data.replace('[ edit ]', '')

def graph_plot(data):
    k,v = zip(*data)
    plt.bar(range(len(k)), v)
    plt.xticks(range(len(k)), k, rotation="vertical")
    plt.show()

def cloud_plot_from_freq(data):
    wc = WordCloud(background_color='white', width=800, height=600)
    plt.figure(figsize=(15,7))
    plt.imshow(wc.generate_from_frequencies({ k:v for k,v in data }))

def cloud_plot_from_text(data):
    wc = WordCloud(background_color='white', width=800, height=600)
    plt.figure(figsize=(15,7))
    plt.imshow(wc.generate(data))
    
url = 'https://en.m.wikipedia.org/wiki/Machine_learning'
text = requests.get(url, verify=False).content.decode("utf-8")
# print(text)
parser = MyHTMLParser()
parser.feed(text)
text=parser.res
# print(text[:1000])

extractor = Rake(max_words=2, min_freq=3, min_chars=5)
res = extractor.apply(text)
# print(res)

graph_plot(res)
cloud_plot_from_freq(res)
cloud_plot_from_text(text)
