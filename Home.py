import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image


df_all = pd.read_csv("https://raw.githubusercontent.com/lecuong9x/Sale-Analysist/main/all_data.csv")
df_all['Month'] = df_all['Order Date'].str.slice(start=0, stop =2, step =1)

html_temp = """
        <div style="background-color:#3872fb; padding:10px;border-radius:10px;">
         <h1 style ="color:white; text-align:center;">Tổng quan dữ liệu bán hàng </h1>  
         <h4 style ="color:white; text-align:center;">Năm 2019 </h4> 
        </div>
"""

desc_temp = """
            ### Báo cáo phân tích bán hàng
            Phân tích và trả lời các câu hỏi kinh doanh về dữ liệu bán hàng trong 12 tháng.
            ### Nội dung của ứng dụng
            - Dữ liệu chứa hàng trăm nghìn lượt mua hàng tại cửa hàng điện tử được chia nhỏ theo tháng, loại sản phẩm, chi phí, địa chỉ mua hàng, v.v.
            ### Công việc phải làm
            - Hợp nhất tất cả các bộ dữ liệu thành một bộ dữ liệu 
            - Bỏ các giá trị NaN khỏi DataFrame
            - Xóa các hàng dựa trên một điều kiện
            - Thay đổi kiểu dữ liệu (to_datetime, astype)
            - Trích xuất dữ liệu từ các giá trị
            ### Trả lời các câu hỏi:
            - Tháng tốt nhất để bán hàng là gì? Tháng đó kiếm được bao nhiêu?
            - Thành phố nào bán được nhiều sản phẩm nhất?
            - Chúng ta nên hiển thị quảng cáo vào thời gian nào để tối đa hóa khả năng mua sản phẩm của khách hàng?
            """
int_temp = """
            ###
            - Xóa giá trị trống
            - Xóa giá trị Or trong month
            - Định dạng dữ liệu số tại 2 cột Quantity và Price
            - Tính doanh số mỗi ID trong ngày (Price * Quantity)
"""
def main(): # trang chính            
    stc.html(html_temp)
    st.markdown(desc_temp, unsafe_allow_html=True)
  

def about(): # trang mô hình hóa
    stc.html(html_temp)
    st.dataframe (df_all)
    with st.expander("Diễn giải dữ liệu"):
            st.dataframe(df_all.describe())

    with st.expander("Loại dữ liệu"):
            st.dataframe(df_all.dtypes)

    with st.expander("Kích cỡ dữ liệu"):
            name = df_all.shape
            # st.dataframe(df_all.shape)
            st.text("Số dòng và cột là {}".format(name))

    with st.expander("Thông tin về các số lượng trường trống"):
            name1 = df_all.isnull().sum()
            st.write(name1)
            #st.text("Số cột trống {}".format(name1))

    with st.expander("Dữ liệu trong trường Month"):
            name2 = df_all['Month'].unique()
            st.write(name2)
    
    with st.expander("Công việc phải làm để làm sạch dữ liệu"):
        st.markdown(int_temp,unsafe_allow_html=True)
            #print(set(df_all['Month']))

page_names_to_funcs = {
    "Trang Chính": main,
    "Thông tin chung về dữ liệu tổng hợp 12 tháng": about,
}
selected_page = st.sidebar.selectbox("Lựa chọn trang", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

