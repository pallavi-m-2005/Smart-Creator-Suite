import streamlit as st

from media_tools import (
    compress_video,
    trim_audio
)

from backup_tool import (
    backup_folder,
    compress_folder,
    restore_backup
)

from system_dashboard import (
    get_system_stats,
    plot_graph
)

from file_watcher import start_watcher

st.title("Media Tools")

video_input = st.text_input("Input Video Path")

video_output = st.text_input("Output Video Path")

if st.button("Compress Video"):

    msg = compress_video(
        video_input,
        video_output
    )

    st.success(msg)


audio_input = st.text_input("Input Audio Path")

audio_output = st.text_input("Output Audio Path")

start_sec = st.number_input(
    "Start Time (seconds)",
    value=0
)

end_sec = st.number_input(
    "End Time (seconds)",
    value=5
)

if st.button("Trim Audio"):

    msg = trim_audio(
        audio_input,
        audio_output,
        start_ms,
        end_ms
    )

    st.success(msg)
