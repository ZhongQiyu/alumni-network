# app.py

import os
import streamlit as st

# 列出文件和目录的函数
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        st.text('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            st.text('{}{}'.format(subindent, f))

# Streamlit app 主体
st.title("百森俱乐部校友卡")

# 个人中心部分
st.header("个人中心")
login_button = st.button("点击登录账号")

if login_button:
    st.info("登录功能待实现")

# 校友卡部分
st.header("百森俱乐部校友卡 Babson China Club")
get_card_button = st.button("立即领取")

if get_card_button:
    st.session_state.show_form = True

# 申领表单部分
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

if st.session_state.show_form:
    st.header("表1: 申领校友卡")
    with st.form("survey_form"):
        name = st.text_input("姓名")
        contact = st.text_input("联系方式")
        occupation = st.text_input("职业信息")
        submit_button = st.form_submit_button("提交")

        if submit_button:
            st.success("表单提交成功")
            # 这里可以处理表单数据，例如发送到服务器
            st.session_state.show_form = False

# 校友会联系方式部分
st.header("校友会联系方式：")
st.write("XXXXXXXXXXXXX")

# 项目文件结构部分
st.header("项目文件结构")
project_dir = "C:\\Users\\xiaoy\\Downloads\\alumni-network"  # 你的项目目录路径
list_files(project_dir)
