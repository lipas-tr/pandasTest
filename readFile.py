import pandas as pd
from collections import OrderedDict

res= []
od = OrderedDict([(":", "/"), (" ", "/"), (",", "/"), (".", "/")])
colnames=['DATE', 'NUMBER'] 
flag=True
counter = 0

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def readAndList(pathofcsv,colnames):
    df = pd.read_csv(pathofcsv,names=colnames, header=None)
    return df

def inputLists(df):
    date1=input("Ilk Tarihi giriniz: ")
    date2=input("Son Tarihi giriniz: ")
    date1.strip()
    date2.strip()
    date1=replace_all(date1,od)
    date2=replace_all(date2,od)
    ids1 = df.index[df['DATE'] == date1].tolist()
    ids2 = df.index[df['DATE'] == date2].tolist()
    return ids1, ids2

def checkList(df,ids1,ids2):
    if len(ids1)== 0 or len(ids2)==0:
        print("girdiginiz tarih degeri dosyada yok! Lutfen tekrar deneyin.")
        ids1,ids2=inputLists(df)
    if ids1>ids2:
        ids1,ids2=ids2,ids1
    return ids1, ids2

def taskResult(df,ids1,ids2):
    df1 = df[ids1[0]:ids2[0]+1]
    max_index = df1['NUMBER'].idxmax()
    min_index = df1['NUMBER'].idxmin()
    maxDate=df1['DATE'][max_index]
    minDate=df1['DATE'][min_index]
    res.extend(df1['NUMBER'].tolist())
    print("ToplamDeger: ", sum(res))
    print("maxDate: ", maxDate)
    print("minDate: ", minDate)

def checkForFinish(counter):
    flagIn=input("bitirmek icin 1'a basiniz: ")
    if flagIn=="1":
        print(counter+". deneme sonucunda cikis yapildi")
        print("Tesekkurler")
        return False
    else:
        return True
df= readAndList("data.csv",colnames)

while flag:
    counter+=1
    ids1, ids2=inputLists(df)
    ids1, ids2=checkList(df,ids1, ids2)
    taskResult(df,ids1,ids2)
    flag=checkForFinish(counter)