from moviepy import editor as mpe


def concat_videos(videos, bg_music, new_fp):
    videos_clip = [mpe.VideoFileClip(v) for v in videos]
    combined_clip = mpe.concatenate_videoclips(videos_clip)

    ori_audio_clip = combined_clip.audio
    # bg_audio_clip = create_bg_music(bg_music, combined_clip.duration)
    bg_audio_clip = mpe.AudioFileClip(bg_music)
    new_audio_clip = mpe.CompositeAudioClip([ori_audio_clip, bg_audio_clip])
    combined_clip.set_audio(new_audio_clip)
    combined_clip.write_videofile(new_fp)


def create_bg_music(music_fp, time_len):
    """
    create an audio with the give time duration. If `time_len` is less than 
    the time-length of the music, cut it from the beginning;
    if `time_len` is greater than music's duration, loop it until satisfied.

    music_fp: file path of music
    time_len: the wanted duration, in seconds
    """
    audio = mpe.AudioFileClip(music_fp)
    if audio.duration < time_len:
        n = int(time_len / audio.duration)
        print("yes")
        audio_clips = [audio for _ in range(n+1)]
        combined_audio = mpe.concatenate_audioclips(audio_clips)
        return combined_audio
    else:
        return audio.subclip(0, time_len)


if __name__ == "__main__":
    videos = ['m.mp4', 'n.mp4']
    bg = 'bg.mp3'
    new_fp = 'hehe.mp4'
    concat_videos(videos, bg, new_fp)


