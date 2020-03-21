import requests
from bs4 import BeautifulSoup

URL = "https://corona.help/"
URL_IMG = "https://en.wikipedia.org/wiki/List_of_sovereign_states_by_date_of_current_flag_adoption"
page_data = requests.get(URL)
page_img = requests.get(URL_IMG)

soup_data = BeautifulSoup(page_data.content, "html.parser")
soup_img = BeautifulSoup(page_img.content, "html.parser")

th= soup_data.find_all('th')
tr= soup_data.find_all('tr')


keys = []
values = []
for i in th:
    keys.append(i.text)

data = []
covid_dict = dict()


l = []

for k in tr:
    data.append(k.text.split())

for v in data[1:]:
    country = ' '.join(v[:-4])
    data = v[-4:]
    covid_dict = {
        "country": country,
        "data": data
    }

   
    l.append(covid_dict)

