# -*- coding: utf-8 -*-

import streamlit as st

st.subheader('ポケモン育成サポーター')

way = st.selectbox('振り方を選択してください',('ドーピングのみ', '野生+ドーピング', '野生のみ'))

    
h = st.slider('HP努力値', 0, 252, 4)

a = st.slider('攻撃努力値', 0, 252, 252)

b = st.slider('防御努力値', 0, 252, 0)    

c = st.slider('特攻努力値', 0, 252, 0)

d = st.slider('特防努力値', 0, 252, 0)

s = st.slider('素早さ努力値', 0, 252, 252)

remainder = 510-h-a-b-c-d-s 

if remainder >= 0:
    st.write('残り努力値'+str(remainder))
    y=1
    
else:
    st.subheader('努力値が最大値を超過しています')
    st.subheader('入力した数値の合計が510以下になるように調整してください')
    y=0
    
if way == 'ドーピングのみ':
    x=1
    
if way == '野生+ドーピング':
    x=2
    
if way == '野生のみ':
    x=3

if x==1 and y==1 and h>0:
    st.write('マックスアップを'+ str((h/10)-(h%10)/10)+ '個、たいりょくのハネを'+ str(h%10)+ '個使ってください')
    
if x==1 and y==1 and a>0:
    st.write('タウリンを'+ str((a/10)-(a%10)/10)+ '個、きんりょくのハネを'+ str(a%10)+ '個使ってください')

if x==1 and y==1 and b>0:
    st.write('ブロムヘキシンを'+ str((b/10)-(b%10)/10)+ '個、ていこうのハネを'+ str(b%10)+ '個使ってください')
    
if x==1 and y==1 and c>0:
    st.write('リゾチウムを'+ str((c/10)-(c%10)/10)+ '個、ちりょくのハネを'+ str(c%10)+ '個使ってください')
    
if x==1 and y==1 and d>0:
    st.write('キトサンを'+ str((d/10)-(d%10)/10)+ '個、せいしんのハネを'+ str(d%10)+ '個使ってください')
    
if x==1 and y==1 and s>0:
    st.write('インドメタシンを'+ str((s/10)-(s%10)/10)+ '個、しゅんぱつのハネを'+ str(s%10)+ '個使ってください')
    
if x==2 and y==1 and h>0:
    st.write('育成したいポケモンにパワーウエイトを持たせてグルトンを'+ str((h-(h%9))/9)+ '体倒し、たいりょくのハネを'+ str(h%9)+ '個使ってください')
    
if x==2 and y==1 and a>0:
    st.write('育成したいポケモンにパワーリストを持たせてヤング―スを'+ str((a-(a%9))/9)+ '体倒し、きんりょくのハネを'+ str(a%9)+ '個使ってください') 
    
if x==2 and y==1 and b>0:
    st.write('育成したいポケモンにパワーベルトを持たせてタマンチュラを'+ str((b-(b%9))/9)+ '体倒し、ていこうのハネを'+ str(b%9)+ '個使ってください')
    
if x==2 and y==1 and c>0:
    st.write('育成したいポケモンにパワーレンズを持たせてデルビルを'+ str((c-(c%9))/9)+ '体倒し、ちりょくのハネを'+ str(c%9)+ '個使ってください')
    
if x==2 and y==1 and d>0:
    st.write('育成したいポケモンにパワーバンドを持たせてハネッコを'+ str((d-(d%9))/9)+ '体倒し、せいしんのハネを'+ str(d%9)+ '個使ってください')
    
if x==2 and y==1 and s>0:
    st.write('育成したいポケモンにパワーアンクルを持たせてディグダを'+ str((s-(s%9))/9)+ '体倒し、しゅんぱつのハネを'+ str(s%9)+ '個使ってください')
    
if x==3 and y==1 and h>0:
    st.write('育成したいポケモンにパワーウエイトを持たせてグルトンを'+ str((h-(h%9))/9)+ '体倒し、アイテムを外してグルトンを'+ str(h%9)+ '体倒してください')
    
if x==3 and y==1 and a>0:
    st.write('育成したいポケモンにパワーリストを持たせてヤング―スを'+ str((a-(a%9))/9)+ '体倒し、アイテムを外してヤング―スを'+ str(a%9)+ '体倒してください')
    
if x==3 and y==1 and b>0:
    st.write('育成したいポケモンにパワーベルトを持たせてタマンチュラを'+ str((b-(b%9))/9)+ '体倒し、アイテムを外してタマンチュラを'+ str(b%9)+ '体倒してください')
    
if x==3 and y==1 and c>0:
    st.write('育成したいポケモンにパワーレンズを持たせてデルビルを'+ str((c-(c%9))/9)+ '体倒し、アイテムを外してデルビルを'+ str(c%9)+ '体倒してください')
    
if x==3 and y==1 and d>0:
    st.write('育成したいポケモンにパワーバンドを持たせてハネッコを'+ str((d-(d%9))/9)+ '体倒し、アイテムを外してハネッコを'+ str(d%9)+ '体倒してください')
    
if x==3 and y==1 and s>0:
    st.write('育成したいポケモンにパワーアンクルを持たせてディグダを'+ str((s-(s%9))/9)+ '体倒し、アイテムを外してディグダを'+ str(s%9)+ '体倒してください')
    
if 'count' not in st.session_state:
  st.session_state["count"] = 0
  
if st.button("カウンター", key=0):
  st.session_state["count"] += 1
  
st.write("倒した数", st.session_state["count"])

if st.button("リセット", key=1):
  st.session_state["count"] = 0