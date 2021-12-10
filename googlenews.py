from pygooglenews import GoogleNews
import pandas as pd

# bisa cari berita diluar negeri dengan cari mengganti singkatan didalam perintah country
gn = GoogleNews(lang = 'id',country = 'ID') 
def get_titles(search):
    datas = []
    search = gn.search(search)
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'judul' : item.title,
            'link': item.link
        }
        datas.append(story)
    return datas

datas = get_titles('militer') #masukan Keyword berita
pd.DataFrame(datas).to_csv("result_Mil.csv") #Memasukan data scrap kedalam csv