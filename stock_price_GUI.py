from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql

try:
    db=pymysql.connect(user='root',password='',host='localhost',database='stock_market')
    mycursor=db.cursor()
except Exception as e:
    print(e)


def data_pro():
    d_d={'01': 0,'02': 1,'03': 2,'04': 3,'05': 4,'06': 5,'07': 6,'08': 7,'09': 8,}
    y_d={}
    j=0
    for i in range(1,32):
        d_d[str(i)]=j
        j+=1
    j=0
    for i in range(2000,2022):
        y_d[str(i)]=j
        j+=1
    return d_d,y_d
        
        
def get_data():
    try:
        bank=e1.get()
        year=e2.get()
        month=e3.get()
        day=e4.get()
        prev=float(e5.get())
        ope=float(e6.get())
        b_d={'HDFC':1, 'AXIS':0, 'KOTAK':4,'ICICI':2,'INDUS':3,'SBI':5}
        d_d,y_d=data_pro()
    
        in_data=[[y_d[year],d_d[month],d_d[day],b_d[bank],prev,ope]]
        pr=lmodel.predict(in_data)
        l7=Label(root,text=f"Highest {round(pr[0][0],2)}     Lowest {round(pr[0][1],2)}",width=60,
             font=("Comic Sans MS",10),bg=clr,fg="black")
        l7.grid()
        data=(bank,year,month,day,prev,ope,round(float(pr[0][0]),2),round(float(pr[0][1]),2))
        query="insert into stockdata_f values(%s,%s,%s,%s,%s,%s,%s,%s)"
    except Exception as e:
        print(e)
    try:
        print(round(pr[0][0],2),round(pr[0][1],2))
        mycursor.execute(query,data)
        db.commit()
        print('done........')
    except Exception as e:
        print(e)

    
HDFC=pd.read_csv(r'G:DS_data/sm_HDFCBANK.csv')
AXIS=pd.read_csv(r'G:DS_data\sm_AXISBANK.csv')
ICICI=pd.read_csv(r'G:DS_data\sm_ICICIBANK.csv')
KOTAK=pd.read_csv(r'G:DS_data\sm_KOTAKBANK.csv')
SBI=pd.read_csv(r'G:DS_data\sm_SBIN.csv')
INDUS=pd.read_csv(r'G:DS_data\sm_INDUSINDBK.csv')
BANK=pd.concat([HDFC,AXIS,ICICI,KOTAK,SBI,INDUS])
BANK=BANK.drop(['Trades', 'Deliverable Volume','%Deliverble'],axis=1)
BANK.replace(['UTIBANK','KOTAKBANK'],['AXISBANK','KOTAKMAH'],inplace=True)

li=[]
import re
for i in BANK.Date:
    li.append(re.split('-',i))
    

    
myd=pd.DataFrame(data=li,columns=['Year','Month','Day'])    
BANK['Year']=myd['Year']
BANK['Month']=myd['Month']
BANK['Day']=myd['Day']    
newdata=BANK.drop(['Date','Series'],axis=1)  

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
newdata['Symbol']=le.fit_transform(np.array(newdata['Symbol']).reshape(-1,1))
newdata['Year']=le.fit_transform(np.array(newdata['Year']).reshape(-1,1))
newdata['Month']=le.fit_transform(np.array(newdata['Month']).reshape(-1,1))
newdata['Day']=le.fit_transform(np.array(newdata['Day']).reshape(-1,1))

X=newdata[['Year','Month','Day','Symbol','Prev Close','Open']]
y=newdata[['High','Low',]] 
print(X.head())
   
from sklearn.linear_model import LinearRegression
lmodel=LinearRegression()
lmodel.fit(X,y)


win=Tk()
win.title("Stock Market Prediction")
win.config(bg="brown2")
root=Frame(win,bg="brown2",bd=15)
root.pack(side=RIGHT,fill=Y)


clr="brown2"

label1=Label(root,text="Enter Market Details",font=("Comic Sans MS",20),bg=clr,fg="black")
label1.grid()

l1=Label(root,text="BANK NAME",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l1.grid()
e1=ttk.Combobox(root,state="readonly",font=10,width=30)
e1['value']=('HDFC', 'AXIS', 'KOTAK','ICICI','INDUS','SBI')
e1.current(0)    
e1.grid()

l2=Label(root,text="Year (2000-2021)",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l2.grid()
e2=Entry(root,bg="white",font=20,width=30)
e2.grid()

l3=Label(root,text="Month",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l3.grid()
e3=Entry(root,bg="white",font=20,width=30)
e3.grid()


l4=Label(root,text="Day",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l4.grid()
e4=Entry(root,bg="white",font=20,width=30)
e4.grid()

l5=Label(root,text="Previous Close",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l5.grid()
e5=Entry(root,bg="white",font=20,width=30)
e5.grid()

l6=Label(root,text="Today's Opening",width=30,font=("Comic Sans MS",10),bg=clr,fg="black")
l6.grid()
e6=Entry(root,bg="white",font=20,width=30)
e6.grid()

b1=Button(root,text="Check High/Low",bg="slateGray2",width=20,font=("bold",10),
                   command=get_data)
b1.grid()

win.mainloop()