# import streamlit as st
# import yt_dlp
# import os
# import re
# from datetime import datetime
# import base64
# from io import BytesIO
# import time
# st.set_page_config(
#     page_title="YT Downloader Pro",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# st.markdown("""
# <style>
#     .main-header {
#         font-size: 3.5rem;
#         background: linear-gradient(90deg, #FF0000, #FF6B6B);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         text-align: center;
#         margin-bottom: 2rem;
#         font-weight: 900;
#     }
#         .sub-header {
#         font-size: 1.8rem;
#         color: #FF4B4B;
#         margin-bottom: 1rem;
#         border-bottom: 3px solid #FF4B4B;
#         padding-bottom: 0.5rem;
#     }
#     </style>
#             """, unsafe_allow_html=True
#             )
# # Title and description
# st.markdown('<h1 class="main-header">🎬 YT Downloader Pro</h1>', unsafe_allow_html=True)
# st.markdown("### The Interactive YouTube Downloader with Premium Features")

# st.markdown('<h2 class="sub-header">📥 Download Center</h2>', unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.markdown('<div class="column-box">', unsafe_allow_html=True)
# #     st.markdown("### 🔗 URL Input")
# #     youtube_url = st.text_input(
# #         "Enter YouTube URL",
# #         placeholder="https://www.youtube.com/watch?v=...",
# #         label_visibility="collapsed"
# #     )
    
# #     # URL validation
# #     if youtube_url:
# #         if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', youtube_url):
# #             st.error("❌ Please enter a valid YouTube URL")
# #         else:
# #             st.success("✅ Valid YouTube URL")
    
# with col1:
#     st.markdown('<div class="column-box">', unsafe_allow_html=True)
#     st.markdown("### 🔗 URL Input")

#     youtube_url = st.text_input(
#         "Enter YouTube URL",
#         placeholder="https://www.youtube.com/watch?v=...",
#         label_visibility="collapsed"
#     )

#     # URL validation
#     if youtube_url:
#         if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', youtube_url):
#             st.error("❌ Please enter a valid YouTube URL")
#         else:
#             st.success("✅ Valid YouTube URL")

#     # ---------- EXTRA FEATURES INSIDE COLUMN 1 ----------
#     st.markdown("---")

#     with st.expander("🎯 Batch Download", expanded=False):
#         st.write("Download multiple videos at once")
#         batch_urls = st.text_area(
#             "Enter multiple URLs (one per line)",
#             placeholder="https://youtu.be/...\nhttps://youtu.be/..."
#         )
#         if st.button("Add to Batch", key="batch"):
#             if batch_urls.strip():
#                 st.success("✅ Added to batch queue!")
#             else:
#                 st.warning("⚠️ Please enter at least one URL")

#     with st.expander("📁 Playlist Download", expanded=False):
#         st.write("Download entire playlists")
#         playlist_url = st.text_input(
#             "Playlist URL",
#             placeholder="https://www.youtube.com/playlist?list=..."
#         )
#         if st.button("Fetch Playlist", key="playlist"):
#             if playlist_url:
#                 st.info("📄 Playlist detected (logic can be added)")
#             else:
#                 st.warning("⚠️ Enter a playlist URL")

#     st.markdown('</div>', unsafe_allow_html=True)


# with col2:
#     st.markdown('<div class="column-box">', unsafe_allow_html=True)
#     st.markdown("### 🎯 Download Type")
    
#     download_type = st.radio(
#         "Select what to download:",
#         ["🎬 Video + Audio", "🎵 Audio Only", "📼 Default"],
#         index=0
#     )
    


# with col3:
#     st.markdown('<div class="column-box">', unsafe_allow_html=True)
#     st.markdown("### 🎚️ Quality Control")
    
#     # Video quality selector
#     if download_type == "🎬 Video + Audio":
#         quality = st.selectbox(
#             "Video Quality",
#             ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "Best"]
#         )
    
#     # Audio quality selector
#     elif download_type == "🎵 Audio Only":
#         quality = st.select_slider(
#             "Audio Quality (kbps)",
#             options=[64, 128, 192, 256, 320],
#             value=192
#         )
#     else:
#         quality ='bestvideo+bestaudio/best'
#         st.subheader('Best Format')


# # Divider
# st.markdown("---")

# # Download section in two columns
# col_left, col_right = st.columns([2, 1])

# # Meta Datas....

# def fetch_video_info(url):
#     ydl_opts = {
#         'quiet': True,
#         'skip_download': True,
#         'noplaylist': True,
#         'ffmpeg_location': r'C:\Program Files\ffmpeg\bin',  # safe even if not used
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)

#     return {
#         'title': info.get('title'),
#         'duration': info.get('duration'),
#         'views': info.get('view_count'),
#         'uploader': info.get('uploader'),
#         'thumbnail': info.get('thumbnail'),
#         'upload_date': info.get('upload_date'),
#     }

# with col_left:
#     if youtube_url and st.button("🔍 Fetch Video Info", use_container_width=True):
#         with st.spinner("Fetching video information..."):
#             try:
#                 video_info = fetch_video_info(youtube_url)
#                 st.session_state.video_info = video_info

#                 st.markdown('<div class="download-info">', unsafe_allow_html=True)
#                 st.markdown("### 📺 Video Information")

#                 # Thumbnail
#                 if video_info['thumbnail']:
#                     st.image(video_info['thumbnail'], use_container_width=True)

#                 col_info1, col_info2, col_info3 = st.columns(3)

#                 with col_info1:
#                     duration_sec = video_info['duration']
#                     minutes = duration_sec // 60
#                     seconds = duration_sec % 60
#                     st.metric("Duration", f"{minutes}:{seconds:02d}")

#                 with col_info2:
#                     views = video_info['views']
#                     st.metric("Views", f"{views:,}" if views else "N/A")

#                 with col_info3:
#                     st.metric("Uploader", video_info['uploader'])

#                 st.markdown(f"**Title:** {video_info['title']}")
#                 st.markdown('</div>', unsafe_allow_html=True)

#             except Exception as e:
#                 st.error("❌ Failed to fetch video info")
#                 st.exception(e)


# def download_video(url, download_type, quality):
#     os.makedirs("downloads", exist_ok=True)

#     output_template = "downloads/%(title)s.%(ext)s"

#     if download_type == "🎵 Audio Only":
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'outtmpl': output_template,
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': str(quality),
#             }],
#         }

#     elif download_type == "🎬 Video + Audio":
#         if quality == "Best":
#             fmt = "bestvideo+bestaudio/best"
#         else:
#             height = quality.replace("p", "")
#             fmt = f"bestvideo[height<={height}]+bestaudio/best"

#         ydl_opts = {
#             'format': fmt,
#             'outtmpl': output_template,
#             'merge_output_format': 'mp4',
#         }

#     else:
#         ydl_opts = {
#             'format': 'best',
#             'outtmpl': output_template,
#         }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         filename = ydl.prepare_filename(info)

#         # If audio-only, extension changes to .mp3
#         if download_type == "🎵 Audio Only":
#             filename = filename.rsplit(".", 1)[0] + ".mp3"

#     return filename


# # with col_right:
# #     # Download button section
# #     st.markdown("### ⬇️ Download Section")
    
# #     if st.button("🚀 DOWNLOAD NOW", type="primary", use_container_width=True):
# #         if not youtube_url:
# #             st.error("❌ Please enter a YouTube URL first!")
# #         else:
# #             # Show progress
# #             progress_bar = st.progress(0)
# #             status_text = st.empty()
            
# #             # Simulate download progress
# #             for percent_complete in range(0, 101, 10):
# #                 time.sleep(0.1)
# #                 progress_bar.progress(percent_complete)
# #                 status_text.text(f"Downloading... {percent_complete}%")
            
# #             # Complete
# #             progress_bar.progress(100)
# #             status_text.text("✅ Download Complete!")
            
# #             # Show success message
# #             st.balloons()
# #             st.markdown('<div class="success-message">', unsafe_allow_html=True)
# #             st.markdown("### 🎉 Download Successful!")
# #             st.markdown(f"**Type:** {download_type} | **Quality:** {video_quality}")
# #             st.markdown("File saved to: `downloads/` folder")
# #             st.markdown('</div>', unsafe_allow_html=True)
            
# #             # Create download button for the file
# #             st.download_button(
# #                 label="📥 Download File",
# #                 data=b"Simulated file content - In real app, this would be actual video data",
# #                 file_name="video_download.mp4",
# #                 mime="video/mp4",
# #                 use_container_width=True
# #             )

# # with col_right:
# #     st.markdown("### ⬇️ Download Section")

# #     if st.button("🚀 DOWNLOAD NOW", type="primary", use_container_width=True):
# #         if not youtube_url:
# #             st.error("❌ Please enter a YouTube URL first!")
# #         else:
# #             try:
# #                 progress_bar = st.progress(0)
# #                 status_text = st.empty()

# #                 status_text.text("⏳ Preparing download...")
# #                 progress_bar.progress(20)

# #                 download_video(youtube_url, download_type, quality)

# #                 progress_bar.progress(100)
# #                 status_text.text("✅ Download Complete!")

# #                 st.balloons()
# #                 st.success("🎉 File downloaded successfully!")
# #                 st.markdown("📂 **Saved in:** `downloads/` folder")

# #             except Exception as e:
# #                 st.error("❌ Download failed")
# #                 st.exception(e)

# with col_right:
#     st.markdown("### ⬇️ Download Section")

#     if st.button("🚀 DOWNLOAD NOW", type="primary", use_container_width=True):
#         if not youtube_url:
#             st.error("❌ Please enter a YouTube URL first!")
#         else:
#             try:
#                 with st.spinner("Downloading..."):
#                     file_path = download_video(youtube_url, download_type, quality)

#                 st.success("🎉 Download ready!")

#                 with open(file_path, "rb") as f:
#                     file_bytes = f.read()

#                 file_name = os.path.basename(file_path)

#                 st.download_button(
#                     label="📥 Click to Download File",
#                     data=file_bytes,
#                     file_name=file_name,
#                     mime="video/mp4" if file_name.endswith(".mp4") else "audio/mpeg",
#                     use_container_width=True
#                 )

#             except Exception as e:
#                 st.error("❌ Download failed")
#                 st.exception(e)

import streamlit as st
import yt_dlp
import os
import re
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="YT Downloader Pro",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main-header {
    font-size: 3.5rem;
    background: linear-gradient(90deg, #FF0000, #FF6B6B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    font-weight: 900;
}
.sub-header {
    font-size: 1.8rem;
    color: #FF4B4B;
    border-bottom: 3px solid #FF4B4B;
    margin-bottom: 1rem;
}
.column-box {
    padding: 1.2rem;
    border-radius: 12px;
    background: #111;
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 class="main-header">🎬 YT Downloader Pro</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">📥 Download Center</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# ---------------- COLUMN 1 ----------------
with col1:
    st.markdown('<div class="column-box">', unsafe_allow_html=True)
    st.markdown("### 🔗 URL Input")

    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed"
    )

    if youtube_url:
        if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', youtube_url):
            st.error("❌ Invalid YouTube URL")
        else:
            st.success("✅ Valid URL")

    st.markdown("---")

    with st.expander("🎯 Batch Download"):
        batch_urls = st.text_area("Multiple URLs (one per line)")
        if st.button("Add to Batch"):
            st.success("Batch added (logic ready)")

    with st.expander("📁 Playlist Download"):
        playlist_url = st.text_input(
            "Playlist URL",
            placeholder="https://www.youtube.com/playlist?list=...",
            key="playlist_url"
        )
        if st.button("Fetch Playlist"):
            st.info("Playlist support ready")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- COLUMN 2 ----------------
with col2:
    st.markdown('<div class="column-box">', unsafe_allow_html=True)
    st.markdown("### 🎯 Download Type")

    download_type = st.radio(
        "Select",
        ["🎬 Video + Audio", "🎵 Audio Only", "📼 Default"]
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- COLUMN 3 ----------------
with col3:
    st.markdown('<div class="column-box">', unsafe_allow_html=True)
    st.markdown("### 🎚️ Quality Control")

    if download_type == "🎬 Video + Audio":
        quality = st.selectbox(
            "Video Quality",
            ["144p", "240p", "360p", "480p", "720p", "1080p", "Best"]
        )
    elif download_type == "🎵 Audio Only":
        quality = st.select_slider(
            "Audio Quality (kbps)",
            options=[64, 128, 192, 256, 320],
            value=192
        )
    else:
        quality = "best"

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
col_left, col_right = st.columns([2, 1])

# ---------------- FETCH META ----------------
def fetch_video_info(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "duration": info.get("duration") or 0,
        "views": info.get("view_count"),
        "uploader": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
    }

with col_left:
    if youtube_url and st.button("🔍 Fetch Video Info", use_container_width=True):
        with st.spinner("Fetching video info..."):
            try:
                data = fetch_video_info(youtube_url)

                if data["thumbnail"]:
                    st.image(data["thumbnail"], use_container_width=True)

                m, s = divmod(data["duration"], 60)

                c1, c2, c3 = st.columns(3)
                c1.metric("Duration", f"{m}:{s:02d}")
                c2.metric("Views", f"{data['views']:,}" if data["views"] else "N/A")
                c3.metric("Uploader", data["uploader"])

                st.markdown(f"**Title:** {data['title']}")

            except Exception as e:
                st.error("Failed to fetch video info")
                st.exception(e)

# ---------------- DOWNLOAD ----------------
def download_video(url, dtype, quality):
    os.makedirs("downloads", exist_ok=True)
    outtmpl = "downloads/%(title)s.%(ext)s"

    # ✅ STREAMLIT-CLOUD SAFE OPTIONS
    if dtype == "🎵 Audio Only":
        # Download best available audio file AS-IS (no mp3 conversion)
        opts = {
            "format": "bestaudio",
            "outtmpl": outtmpl,
        }

    elif dtype == "🎬 Video + Audio":
        if quality == "Best":
            fmt = "best[ext=mp4]/best"
        else:
            height = quality[:-1]  # "720p" -> "720"
            fmt = f"best[height<={height}][ext=mp4]/best"

        opts = {
            "format": fmt,
            "outtmpl": outtmpl,
        }

    else:
        opts = {
            "format": "best",
            "outtmpl": outtmpl,
        }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename


# ---------------- DOWNLOAD UI ----------------
mime = with col_right:
    st.markdown("### ⬇️ Download")

    if st.button("🚀 DOWNLOAD NOW", type="primary", use_container_width=True):
        if not youtube_url:
            st.error("Enter a URL first")
        else:
            try:
                with st.spinner("Downloading..."):
                    path = download_video(youtube_url, download_type, quality)

                mime = "video/mp4" if path.endswith(".mp4") else "audio/webm"

                with open(path, "rb") as f:
                    st.download_button(
                        "📥 Download File",
                        f.read(),
                        file_name=os.path.basename(path),
                        mime=mime,
                        use_container_width=True
                    )

                st.success("✅ Download complete!")

            except Exception as e:
                st.error("❌ Download failed")
                st.exception(e)


