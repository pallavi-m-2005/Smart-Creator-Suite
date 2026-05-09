import streamlit as st
import psutil
import time

from system_dashboard import (
    get_system_stats,
    plot_graph
)

from backup_tool import (
    backup_folder,
    compress_folder,
    restore_backup
)

from file_watcher import start_watcher

from media_tools import (
    compress_video,
    trim_audio
)


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

    if stats["CPU"] > 80:
        st.warning("⚠ High CPU Usage!")

    cpu_data = []
    ram_data = []

    for i in range(5):

        cpu_data.append(psutil.cpu_percent())

        ram_data.append(
            psutil.virtual_memory().percent
        )

        time.sleep(1)

    st.subheader("CPU Usage Graph")

    cpu_fig = plot_graph(cpu_data, "CPU Usage")

    st.pyplot(cpu_fig)

    st.subheader("RAM Usage Graph")

    ram_fig = plot_graph(ram_data, "RAM Usage")

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

    st.subheader("Compress Backup Folder")

    folder_to_compress = st.text_input(
        "Folder Path to Compress"
    )

    if st.button("Compress Folder"):

        try:

            zip_path = compress_folder(
                folder_to_compress
            )

            st.success(
                f"Compressed File:\n{zip_path}"
            )

        except Exception as e:

            st.error(str(e))

    st.subheader("Restore Backup")

    zip_file = st.text_input(
        "ZIP File Path"
    )

    restore_path = st.text_input(
        "Restore Destination"
    )

    if st.button("Restore Backup"):

        try:

            msg = restore_backup(
                zip_file,
                restore_path
            )

            st.success(msg)

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

    st.subheader("Video Compression")

    video_input = st.text_input(
        "Input Video Path"
    )

    video_output = st.text_input(
        "Output Video Path"
    )

    if st.button("Compress Video"):

        try:

            msg = compress_video(
                video_input,
                video_output
            )

            st.success(msg)

        except Exception as e:

            st.error(str(e))

    st.subheader("Audio Trimming")

    audio_input = st.text_input(
        "Input Audio Path"
    )

    audio_output = st.text_input(
        "Output Audio Path"
    )

    start_ms = st.number_input(
        "Start Time (milliseconds)",
        value=0
    )

    end_ms = st.number_input(
        "End Time (milliseconds)",
        value=5000
    )

    if st.button("Trim Audio"):

        try:

            msg = trim_audio(
                audio_input,
                audio_output,
                start_ms,
                end_ms
            )

            st.success(msg)

        except Exception as e:

            st.error(str(e))
