import pandas as pd
import time
import timeit
import numpy as np
path ='C:\Documents\Documents\Loblaw\Image-Compare-master\Image-Compare.csv'
df = pd.read_csv(path)
print(df.head(10))
print(df.columns)
url1=df['Image1'].values.tolist()
url2=df['Image2'].values.tolist()
p_diff=[]
tl_e=[]
result=[]
print(len(df))
for (url_1,url_2) in zip(url1,url2):
    start = time.time()
    with open(url_1,'rb') as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
    Image_1 = Image.open('temp.jpg')
    with open(url_2,'rb') as url:
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
    #result.append(np.where((dif / 255.0 * 100) / ncomponents < 15, 'Passed','Failed-Not Similar'))
df['similar']=p_diff
df['elapsed']=tl_e
print(df.head())
#df['Results']=result
df.to_csv('C:\Documents\Documents\Loblaw\Image-Compare-master\Results.csv')