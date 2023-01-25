import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as stc
import plotly_express as px
import altair as alt
from PIL import Image

desc_temp = """
            Họ tên: Lê Cảnh Cường
            - SĐT: 0387688878
            - Mail: strongpower9x@gmail.com
            """

inf = """
    Tóm tắt về bản thân:
    - Có 3+ năm kinh nghiệm trong lĩnh vực tài chính ngân hàng
    - Phân tích và tổng hợp số liệu tài chính tốt, thành thạo các ngôn nghữ lập trình/phần mềm như Excel, VBA, SQL, Python
    - Chăm chỉ, có trách nhiệm trong công việc

"""

left_column, right_column = st.columns([2,3])
with left_column:
    img = Image.open("https://github.com/lecuong9x/Sale-Analysist/blob/main/image1.jpg")
    st.image(img,use_column_width = True)
    

# with mid_column:
#     pass

with right_column:
    st.subheader(desc_temp)

st.subheader(inf)    


