import streamlit as st
import psutil
import time

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


st.set_page_config(
    page_title="Smart Creator Suite",
    layout="wide"
)

st.title("🧠 Smart Creator & System Automation Suite")


menu = st.sidebar.selectbox(
    "Select Module",
    [
        "System Dashboard",
        "Backup Tool",
        "File Watcher",
        "Media Tools"
    ]
)

# ---------------------------------------------------
# SYSTEM DASHBOARD
# ---------------------------------------------------

if menu == "System Dashboard":

    st.header("🖥 System Health Dashboard")

    stats = get_system_stats()

    col1, col2, col3 = st.columns(3)

    col1.metric("CPU Usage", f"{stats['CPU']}%")
    col2.metric("RAM Usage", f"{stats['RAM']}%")
    col3.metric("Disk Usage", f"{stats['Disk']}%")

    cpu_data = []
    ram_data = []

    for i in range(5):

        cpu_data.append(psutil.cpu_percent())

        ram_data.append(
            psutil.virtual_memory().percent
        )

        time.sleep(1)

    st.subheader("CPU Usage Graph")

    cpu_fig = plot_graph(
        cpu_data,
        "CPU Usage"
    )

    st.pyplot(cpu_fig)

    st.subheader("RAM Usage Graph")

    ram_fig = plot_graph(
        ram_data,
        "RAM Usage"
    )

    st.pyplot(ram_fig)

# ---------------------------------------------------
# BACKUP TOOL
# ---------------------------------------------------

elif menu == "Backup Tool":

    st.header("💾 Backup & Restore Tool")

    source = st.text_input(
        "Enter Source Folder Path"
    )

    destination = st.text_input(
        "Enter Backup Destination Path"
    )

    if st.button("Create Backup"):

        try:

            backup_path = backup_folder(
                source,
                destination
            )

            st.success(
                f"Backup Created:\n{backup_path}"
            )

        except Exception as e:

            st.error(str(e))

# ---------------------------------------------------
# FILE WATCHER
# ---------------------------------------------------

elif menu == "File Watcher":

    st.header("👀 File Watcher Automation")

    source_folder = st.text_input(
        "Folder To Watch"
    )

    target_folder = st.text_input(
        "Move Files To"
    )

    if st.button("Start Watching"):

        try:

            observer = start_watcher(
                source_folder,
                target_folder
            )

            st.success(
                "Watcher Started Successfully!"
            )

        except Exception as e:

            st.error(str(e))

# ---------------------------------------------------
# MEDIA TOOLS
# ---------------------------------------------------

elif menu == "Media Tools":

    st.header("🎬 Media Tools")

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
