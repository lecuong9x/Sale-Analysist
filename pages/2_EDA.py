import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as stc
import plotly_express as px
import altair as alt

# df_all = pd.read_csv("https://raw.githubusercontent.com/lecuong9x/Sale-Analysist/main/all_data.csv")
# df_all['Month'] = df_all['Order Date'].str.slice(start=0, stop =2, step =1)


html_temp = """
        <div style="background-color:#3872fb; padding:10px;border-radius:10px;">
         <h1 style ="color:white; text-align:center;">Tổng quan dữ liệu bán hàng </h1>  
         <h4 style ="color:white; text-align:center;">Năm 2019 </h4> 
        </div>
"""
# remove nan 
# df_all1 = df_all.dropna(how="all")
# df_all2 = df_all1[df_all1['Month'] != 'Or'] # loai gia tri Or

# tách cột city từ cột purchase address
# address_to_city = lambda address:address.split(',')[1]
# df_all2['City'] = df_all2['Purchase Address'].apply(address_to_city)
# df_all2['Quantity Ordered'] = pd.to_numeric(df_all2['Quantity Ordered'], downcast = 'float')
# df_all2['Price Each'] = pd.to_numeric(df_all2['Price Each'], downcast = 'float')
# df_all2['Sales'] = df_all2['Quantity Ordered'] *df_all2['Price Each']
# df_all2['Order Date'] = pd.to_datetime(df_all2['Order Date'],errors= "coerce")
# df_all2 = df_all2.assign(hour = df_all2["Order Date"].dt.hour)
df_all2 = pd.read_csv("https://raw.githubusercontent.com/lecuong9x/Sale-Analysist/main/sale.csv")

stc.html(html_temp)

st.sidebar.header("Filter here:")

City = st.sidebar.multiselect(
    "Chọn tên thành phố:",
    options=df_all2["City"].unique(),
    default=df_all2["City"].unique()
)

Month = st.sidebar.multiselect(
    "Chọn tháng:",
    options=df_all2["Month"].unique(),
    default=df_all2["Month"].unique()
)

# https://www.youtube.com/watch?v=Sb0A9i6d320&list=PLHgX2IExbFovFg4DI0_b3EWyIGk-oGRzq
df_selection = df_all2.query("City == @City") #& Month == @Month"


#---- main page
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

#top 

total_sales = int(df_selection["Sales"].sum())
average_sales = round(df_selection["Sales"].mean(),1)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Tổng Doanh Thu:")
    st.success(f'US $ {total_sales:,}')

with right_column:
    st.subheader("Doanh thu trung bình:")
    st.success(f'US $ {average_sales:,}')

st.markdown("____")
sale_by_product = (
    df_selection.groupby(["Product"]).sum().sort_values("Sales",ascending=True)
)

st.success("Doanh số theo từng sản phẩm")
fig_product_salses = px.bar(
    sale_by_product,
    x = "Sales",
    y = sale_by_product.index,
    orientation = "h",
    #title = "<B>Doanh số theo từng sản phẩm",
    color_discrete_sequence = ["chartreuse"]*len(sale_by_product),
    template= "plotly_white"
)
st.plotly_chart(fig_product_salses)

st.success("Doanh số theo thành phố")
sale_by_city = (
    df_selection.groupby("City").sum().sort_values("Sales", ascending=True)
)

fig_city_salses = px.bar(
    sale_by_city,
    x = "Sales",
    y = sale_by_city.index,
    orientation = "h",
    #title = "<B>Doanh số theo thành phố",
    color_discrete_sequence = ["thistle"]*len(sale_by_city),
    template= "plotly_white"
)
st.plotly_chart(fig_city_salses)

sale_by_hour = (
    df_selection.groupby("Hours")
    .agg({"Sales":"sum"})
)

st.line_chart(sale_by_hour,use_container_width=True)

sale_product = df_selection.groupby('Product').sum()['Quantity Ordered']
prices =df_selection.groupby('Product').mean()['Price Each']

st.success("Thời điểm trong năm bán hàng được nhiều")
sale_by_month = (
    df_all2.groupby("Month").agg({"Sales":"sum"})
)
#st.write(sale_by_month)
st.line_chart(sale_by_month,use_container_width=True)

st.success("Thời điểm trong ngày bán hàng được nhiều")
