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

uploaded_video = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video is not None:

    input_path = uploaded_video.name

    with open(input_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    output_path = "compressed_video.mp4"

    if st.button("Compress Video"):

        try:

            msg = compress_video(
                input_path,
                output_path
            )

            st.success(msg)

            with open(output_path, "rb") as file:
                st.download_button(
                    "Download Compressed Video",
                    file,
                    file_name="compressed_video.mp4"
                )

        except Exception as e:

            st.error(str(e))
            
uploaded_audio = st.file_uploader(
    "Upload Audio",
    type=["mp3", "wav"]
)

start_sec = st.number_input(
    "Start Time (seconds)",
    value=0
)

end_sec = st.number_input(
    "End Time (seconds)",
    value=5
)

if uploaded_audio is not None:

    input_audio_path = uploaded_audio.name

    with open(input_audio_path, "wb") as f:
        f.write(uploaded_audio.getbuffer())

    output_audio_path = "trimmed_audio.mp3"

    if st.button("Trim Audio"):

        try:

            msg = trim_audio(
                input_audio_path,
                output_audio_path,
                start_sec,
                end_sec
            )

            st.success(msg)

            with open(output_audio_path, "rb") as file:
                st.download_button(
                    "Download Trimmed Audio",
                    file,
                    file_name="trimmed_audio.mp3"
                )

        except Exception as e:

            st.error(str(e))
