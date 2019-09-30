import pandas as pd
import time
import imagehash
import timeit
from PIL import Image
import numpy as np
import urllib.request
url = 'https://raw.githubusercontent.com/harshavijay85/Image-Compare/master/Image-Compare.csv'
df=pd.DataFrame()
df = pd.read_csv(url)
print(df.head(10))
print(df.columns)
url1=df['Image1'].values.tolist()
url2=df['Image2'].values.tolist()
p_diff=[]
tl_e=[]
result=[]
print(len(df))
for (url_1,url_2) in zip(url1,url2):
    #url1 = "https://github.com/harshavijay85/Image-Compare/blob/master/GitDog-2?raw=true"
    #url2 = "https://github.com/harshavijay85/Image-Compare/blob/master/GitDog-1?raw=true"
    start = time.time()
    with urllib.request.urlopen(url_1) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
    Image_1 = Image.open('temp.jpg')
    with urllib.request.urlopen(url_2) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
    Image_2 = Image.open('temp.jpg')
    i1 = Image_1
    i2 = Image_2
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
        ncomponents = i1.size[0] * i1.size[1] * 3
        print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
        end = time.time()
        print("Elapsed time",end - start)
    p_diff.append((dif / 255.0 * 100) / ncomponents)
    tl_e.append(end-start)
    result.append(np.where((dif / 255.0 * 100) / ncomponents < 15, 'Passed','Failed-Not Similar'))
df['Percent_Diff']=p_diff
df['Time_Elapsed']=tl_e
df['Results']=result
df.to_csv('Results.csv')