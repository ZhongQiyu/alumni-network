# app.py

import os
import datetime
import streamlit as st

# 日志记录函数
def log_message(message):
    log_file = os.path.join(os.path.dirname(__file__), '../temp/OneDC_Updater/update.log')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as file:
        file.write(f"{timestamp} - {message}\n")

# 更新函数
def perform_update():
    log_message("Update started")
    
    try:
        # 模拟下载新数据
        log_message("Connecting to data source")
        # 假设这里是下载数据的代码
        log_message("Downloaded new data")
        
        # 模拟处理数据
        log_message("Processing data")
        # 假设这里是处理数据的代码
        log_message("Data processed")
        
        log_message("Update completed successfully")
    except Exception as e:
        log_message(f"Update failed: {str(e)}")

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

# 更新日志部分
st.header("更新日志")
if st.button("执行更新"):
    perform_update()
    st.success("更新已执行")

log_file = os.path.join(project_dir, 'temp', 'OneDC_Updater', 'update.log')
with open(log_file, 'r') as file:
    log_contents = file.read()
    st.text(log_contents)

import streamlit as st

# 设置应用标题
st.title("Babson China Club Alumni Card")

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

# 显示 main.html 的内容
st.header("展示 main.html 内容")
with open("main.html", "r", encoding="utf-8") as file:
    html_content = file.read()
st.components.v1.html(html_content, height=600)
