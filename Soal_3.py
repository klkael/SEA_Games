import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
url = 'https://www2.2019seagames.com/countries/'
x = requests.get(url)
soup = BeautifulSoup(x.content,'html.parser')
data = soup.find_all('em')
dataa = []
for i in data:
    dataa.append(i.text)
# print(dataa)
negara = []
gold = []
negaraa = dataa[:66:6]
goldd = dataa[2:66:6]
negara.append(negaraa)
gold.append(goldd)
# print(negaraa) #nama negara
# print(goldd) #jumlah gold 2017
# print(negaraa)
golddd2017 = np.array([0,3,38,2,145,7,24,57,72,0,58])

url = 'https://rs.2019seagames.com/RS2019/mobiapp/MedalTally'
y = requests.get(url)
sup = BeautifulSoup(y.content,'html.parser')
supp = sup.find_all('small')
gold2019 = []
for i in supp:
    gold2019.append(i.text)
gold2019 = gold2019[6::5]
print(gold2019)
golddd2019 = np.array([2,4,72,1,55,4,149,52,92,0,98])

df = pd.DataFrame({
    '2017':[0,3,38,2,145,7,24,57,72,0,58],
    '2019':[2,4,72,1,55,4,149,52,92,0,98],
    'x':negaraa
})
plt.figure('GOLD MEDAL TALLY SEA GAMES 2017 & 2019',figsize=(16,8))
plt.plot(df['x'],df[['2019','2017']])
plt.grid()
plt.legend(['2017','2019'])
plt.title('GOLD MEDAL TALLY SEA GAMES 2017 & 2019')
plt.xticks(rotation=90)
plt.show()

persentase = []
for i in golddd2017:
    asd = i/406
    persentase.append(asd)

explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
plt.pie(persentase,labels=negaraa,explode=explode,textprops={'size':10,'color':'black'},autopct='%1.2f%%')
plt.title('GOLD % SEA GAMES 2017',fontdict={'family':'impact','size':30,'color':'green'})
plt.show()

persentasee = []
for i in golddd2019:
    asd = i/529
    persentasee.append(asd)

explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
plt.pie(persentasee,labels=negaraa,explode=explode,textprops={'size':10,'color':'black'},autopct='%1.2f%%')
plt.title('GOLD % SEA GAMES 2019',fontdict={'family':'impact','size':30,'color':'green'})
plt.show()
