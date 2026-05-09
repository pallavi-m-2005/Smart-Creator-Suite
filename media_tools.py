try:
    from moviepy import VideoFileClip
except ImportError:
    from moviepy.editor import VideoFileClip

from pydub import AudioSegment


def compress_video(input_path, output_path):

    uploaded_video = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi"]
)

    video.write_videofile(
        output_path,
        bitrate="500k"
    )

    video.close()

    return "Video Compressed Successfully"


def trim_audio(input_path, output_path, start_ms, end_ms):

    audio = AudioSegment.from_file(input_path)

    trimmed_audio = audio[start_ms:end_ms]

    trimmed_audio.export(
        output_path,
        format="mp3"
    )

    return "Audio Trimmed Successfully"
