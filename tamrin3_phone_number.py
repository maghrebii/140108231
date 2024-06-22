import streamlit as st
import pandas as pd
import uuid  
from streamlit_gsheets import GSheetsConnection

df = pd.DataFrame({'phone number': ['12345', '67890']})

st.subheader("elham maghrebi Project")
phone_number_gs = st.text_input('شماره تماس')    

conn = st.connection("gsheets", type=GSheetsConnection)
df_gs = conn.read(worksheet="Sheet2", usecols=[0])
new_row_gs = {'phone number': phone_number_gs}

if st.button('ذخیره '):
    df_gs = pd.concat([df_gs, pd.DataFrame([new_row_gs])], ignore_index=True)
    conn.write(df_gs, worksheet="Sheet2")  
    st.success('ذخیره شد ')
    
st.dataframe(df_gs)


#

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def read_data_from_google_sheets():
    df = conn.read(worksheet="Sheet2")  
    return df

def write_data_to_google_sheets(df):
    conn.write(df, worksheet="Sheet2")  

def update_phone_number(df, old_number, new_number):
    idx = df[df['phone number'] == old_number].index
    
    if not idx.empty:
        df.loc[idx, 'phone number'] = new_number
        return True
    else:
        return False

def delete_phone_number(df, number_to_delete):
    idx = df[df['phone number'] == number_to_delete].index
    
    if not idx.empty:
        df.drop(idx, inplace=True)
        df.reset_index(drop=True, inplace=True)  
        return True
    else:
        return False

df = read_data_from_google_sheets()



phone_number_old = st.selectbox('انتخاب شماره تماس برای ویرایش', df['phone number'])

new_phone_number = st.text_input('شماره تماس جدید')

if st.button('ویرایش'):
    if update_phone_number(df, phone_number_old, new_phone_number):
        st.success('شماره با موفقیت ویرایش شد')
        st.dataframe(df)
        
        write_data_to_google_sheets(df)
    else:
        st.error('شماره مورد نظر یافت نشد یا ویرایش ناموفق بود')

phone_number_delete = st.selectbox('انتخاب شماره تماس برای حذف', df['phone number'])

if st.button('حذف'):
    if delete_phone_number(df, phone_number_delete):
        st.success('شماره با موفقیت حذف شد')
        st.dataframe(df)
        
        write_data_to_google_sheets(df)
    else:
        st.error('شماره مورد نظر یافت نشد یا حذف ناموفق بود')

st.dataframe(df)

