try:
    from moviepy import VideoFileClip
except ImportError:
    from moviepy.editor import VideoFileClip

try:
    from moviepy import (
        VideoFileClip,
        AudioFileClip
    )
except ImportError:
    from moviepy.editor import (
        VideoFileClip,
        AudioFileClip
    )


def compress_video(input_path, output_path):

    video = VideoFileClip(input_path)

    video.write_videofile(
        output_path,
        bitrate="500k"
    )

    video.close()

    return "Video Compressed Successfully"


def trim_audio(
    input_path,
    output_path,
    start_sec,
    end_sec
):

    audio = AudioFileClip(input_path)

    trimmed_audio = audio.subclipped(
        start_sec,
        end_sec
    )

    trimmed_audio.write_audiofile(output_path)

    audio.close()
    trimmed_audio.close()

    return "Audio Trimmed Successfully"
