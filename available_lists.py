import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import pandas_bokeh
from astropy.time import Time

df=pd.read_csv('files.csv')
df = pd.DataFrame(df['Lists'].str.split('_').tolist(),
                                 columns = ['location','location2','receiver','date','code'])
location=pd.DataFrame(df['location'].str.split('/').tolist()
                      ,columns=['n','n','n','n','n','n','name','receiver','n','n'])


sc=location['name']
rcv=location['receiver']
date=pd.to_datetime(df['date'],format='%Y%m%d', errors='ignore')
chunck={'source':sc, 'receiver':rcv, 'date':date}
lists=pd.DataFrame(data=chunck, columns=['source','receiver','date'])

from matplotlib.backends.backend_pdf import PdfPages
from pandas.plotting import table

count=lists.groupby(['source','receiver']).count()
late=lists.groupby(['source','receiver']).max()
early=lists.groupby(['source','receiver']).min()

frames={"TOAs": count, "early": early, "late": late}
result = pd.concat(frames,axis=1)
result

with open('dataframe.html', 'w') as outfile:
    outfile.write(result.to_html())
    
import seaborn as sns
sns.set(rc={'figure.figsize':(20,8.27)})
sns.stripplot(y="source",x='date',data=lists,jitter=True,
              hue='receiver',hue_order = ['P217-3', 'P200-3', 'S110-1','S60-2']
              ,palette='Set1')
plt.savefig("dataframe.png")
