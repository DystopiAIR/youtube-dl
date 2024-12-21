import streamlit as st
from downloader import download_video  # 改为导入新的下载函数

st.title('YouTube 视频下载器')

url = st.text_input('请输入YouTube视频链接')
if st.button('下载'):
    if url:
        try:
            result = download_video(url)
            st.success(result)
        except Exception as e:
            st.error(f'下载失败：{str(e)}')
    else:
        st.warning('请输入视频链接') 