import streamlit as st
from downloader import download_video
from pathlib import Path

st.title('YouTube 视频下载器')

url = st.text_input('请输入YouTube视频链接')
if st.button('下载'):
    if url:
        try:
            message, file_path = download_video(url)
            st.success(message)
            
            # 添加下载按钮
            with open(file_path, 'rb') as file:
                st.download_button(
                    label="点击下载视频",
                    data=file,
                    file_name=file_path.name,
                    mime='video/mp4'
                )
            # 删除服务器上的文件
            file_path.unlink()
        except Exception as e:
            st.error(f'下载失败：{str(e)}')
    else:
        st.warning('请输入视频链接')