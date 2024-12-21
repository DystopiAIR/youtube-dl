import yt_dlp
import os

def download_video(url: str) -> str:
    """下载YouTube视频"""
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"成功下载: {info['title']}"
    except Exception as e:
        raise Exception(f"下载失败: {str(e)}") 