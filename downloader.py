import yt_dlp
import os
from pathlib import Path

def download_video(url: str) -> tuple[str, Path]:
    """下载YouTube视频并返回文件路径"""
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            file_path = Path(filename)
            return f"成功下载: {info['title']}", file_path
    except Exception as e:
        raise Exception(f"下载失败: {str(e)}") 