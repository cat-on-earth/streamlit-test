#import部分で波線が出る場合
#https://startlab.jp/learning-python/vscode-settings/

import streamlit as st
import numpy as np
import pandas as pd

#画像を表示させる
from PIL import Image
import time


st.title('strreamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'



st.write('DataFrame')


df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
})

#tableを作る方法
st.write(df)
#dataframeだと引数がいくつか入れることができる
st.dataframe(df)
st.dataframe(df,width=100,height=100)
#列を指定するときはaxis=0,行は1
st.dataframe(df.style.highlight_max(axis=0))
#静的なテーブルを作る時はtableを使う（ソートができない）
st.table(df)

"""
#マジックコマンド
#マークダウン記法
# 章
## 節
### 項

#バッククォーテーションで囲う
```python
import streamlit as st
import munpy as np
import pandas as pd
```

"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
df
#折れ線グラフなど
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100,2),
    columns=['lat', 'lon']
)
df

#東京付近で
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat', 'lon']
)
df

st.map(df)


st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は、', option, 'です。'

#チェックボックスにチェックがあればTrue,なければFalse
if st.checkbox('Show Image'):

    img = Image.open('roppongi.jpeg')
    st.image(img, caption='ROPPONGI', use_column_width=True)



st.write('Interactive Widgets')

'''
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0 ,100, 50)
'コンディション：', condition
'''

'''
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0 ,100, 50)
'あなたの趣味：', text
'コンディション：', condition
'''

left_column, right_column = st.columns(2)
button =left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')




