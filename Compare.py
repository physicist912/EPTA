import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mti
from math import floor, log10
import decimal
def gauss(x,m,sig):
    return np.exp(-((x-m)/sig)**2/2)

def expon(val):
    exp=str(val).split('e')[1]
    return int(exp)

def loc(x,m,sig):
    x=x-m
    return abs(x/sig)

def sig(val,sig):


    if int(val)-val==0:
        return sig*(len(str(val))-1)
    val=abs(val)
    if 'e' in str(val):
        factor=str(val).split('e')
        mag=factor[0]
        pw=factor[1]
    if 'e' not in str(val):
        mag=str(val)
        pw=0
    if '.' in mag:
        mag=mag.split('.')
        
        intnum=mag[0]
        dec=mag[1]
        return float(sig)*10**float(pw)*10**(-len(dec))
    else: 
        mag=mag
        return float(sig)*10**float(pw)
        
        
        
def smarter_round(sig):
    def rounder(x):
        offset = sig - floor(log10(abs(x)))
        initial_result = round(x, offset)
        if str(initial_result)[-1] == '5' and initial_result == x:
            return round(x, offset - 2)
        else:
            return round(x, offset - 1)
    return rounder
    


obj='J1439'
dat=obj+'/'+obj+'.csv'
df = pd.DataFrame(pd.read_csv(dat))

params=list(df['par'])
comp='mk_new'
dcomp='d'+comp
comp2='mk+time+epoch'
dcomp2='d'+comp2
ref='ref'
dref='d'+ref

for i in params:

    m1=float(df[comp][df['par']==i])
    sig1=float(df[dcomp][df['par']==i])
    m3=float(df[comp2][df['par']==i])
    sig3=float(df[dcomp2][df['par']==i])
    
    m2=float(df[ref][df['par']==i].apply(smarter_round(15)))
    sig2=float(df[dref][df['par']==i].apply(smarter_round(15)))
    sig2=(sig(m2,sig2))
    
    val=(m1+m2)/2
    print(i)
    print(m1)
    print(m2)
    print(sig1)
    print(sig2)
    print('=====')
    if sig1>sig2:
        s=sig1
    else:
        s=sig2

    rangp=float(val*2)
   
    x=np.linspace(val-sig2*15,val+sig2*15,50000)

    par1=gauss(x,m1,sig1)
    par2=gauss(x,m2,sig2)
    par3=gauss(x,m3,sig3)
    
    loc4=loc(m2,m3,sig2)
    loc3=loc(m2,m3,sig3)
    loc2=loc(m2,m1,sig1)
    loc1=loc(m2,m1,sig2)
    
    fig, ax = plt.subplots(2,1,figsize=(10,5))
    fig.patch.set_facecolor('white')

    ax[0].title.set_text('%s located at %.3f $\sigma$ from %s\n%s located at %.3f $\sigma$ from %s'%(ref,loc2,comp,comp,loc1,ref))
    ax[0].set_xlim(m2-sig2*10,m2+sig2*10)

    ax[0].plot(x,par1,'g',label='%s (%s)'%(comp,i))
    ax[0].plot([m1+sig1,m1+sig1],[0,1],'c:')
    ax[0].plot([m1-sig1,m1-sig1],[0,1],'c:')
    ax[0].plot([m1+2*sig1,m1+2*sig1],[0,1],'c:')
    ax[0].plot([m1-2*sig1,m1-2*sig1],[0,1],'c:')
    ax[0].plot(x,par2,'b',label='%s (%s)'%(ref,i))
    ax[0].plot([m2+sig2,m2+sig2],[0,1],'r:')
    ax[0].plot([m2-sig2,m2-sig2],[0,1],'r:')
    ax[0].plot([m2+2*sig2,m2+2*sig2],[0,1],'r:')
    ax[0].plot([m2-2*sig2,m2-2*sig2],[0,1],'r:')
    ax[0].legend()
    
    ax[1].title.set_text('%s located at %.3f $\sigma$ from %s\n%s located at %.3f $\sigma$ from %s'%(ref,loc3,comp2,comp2,loc4,ref))
    ax[1].set_xlim(m2-sig2*10,m2+sig2*10)

    ax[1].plot(x,par3,'g',label='%s (%s)'%(comp2,i))
    ax[1].plot([m3+sig3,m3+sig3],[0,1],'c:')
    ax[1].plot([m3-sig3,m3-sig3],[0,1],'c:')
    ax[1].plot([m3+2*sig3,m3+2*sig3],[0,1],'c:')
    ax[1].plot([m3-2*sig3,m3-2*sig3],[0,1],'c:')
    ax[1].plot(x,par2,'b',label='%s (%s)'%(ref,i))
    ax[1].plot([m2+sig2,m2+sig2],[0,1],'r:')
    ax[1].plot([m2-sig2,m2-sig2],[0,1],'r:')
    ax[1].plot([m2+2*sig2,m2+2*sig2],[0,1],'r:')
    ax[1].plot([m2-2*sig2,m2-2*sig2],[0,1],'r:')
    ax[1].legend()
    if m2<1e-2:
        ax[0].xaxis.set_major_formatter(mti.FormatStrFormatter('%.3e'))
        ax[1].xaxis.set_major_formatter(mti.FormatStrFormatter('%.3e'))

    fig.tight_layout()
    plt.savefig(obj+'/%s'%(i)+obj+'.png',dpi=500)
