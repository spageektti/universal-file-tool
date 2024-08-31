from moviepy.editor import TextClip, CompositeVideoClip, vfx, AudioFileClip

def video_operations(file_path):
    """Perform basic video operations."""
    print("1. Get Video Duration")
    print("2. Extract Audio from Video")
    print("3. Concatenate Videos")
    print("4. Resize Video")
    print("5. Add Text to Video")
    print("6. Change Video Speed")
    print("7. Apply Fade-In Effect")
    print("8. Add Background Music")
    print("9. Trim Video")
    print("10. Rotate Video")
    print("11. Apply Fade-Out Effect")
    choice = input("Select option: ")

    if choice == "1":
        try:
            video = VideoFileClip(file_path)
            print(f"Video duration: {video.duration} seconds")
        except Exception as e:
            print(f"Error getting video duration: {e}")

    elif choice == "2":
        try:
            video = VideoFileClip(file_path)
            audio_path = os.path.splitext(file_path)[0] + "_audio.mp3"
            video.audio.write_audiofile(audio_path)
            print(f"Audio extracted successfully: {audio_path}")
        except Exception as e:
            print(f"Error extracting audio: {e}")

    elif choice == "3":
        try:
            video_files = input("Enter video files to concatenate (comma-separated): ").split(",")
            clips = [VideoFileClip(v.strip()) for v in video_files]
            final_clip = concatenate_videoclips(clips)
            output_path = "concatenated_video.mp4"
            final_clip.write_videofile(output_path)
            print(f"Videos concatenated successfully: {output_path}")
        except Exception as e:
            print(f"Error concatenating videos: {e}")

    elif choice == "4":
        try:
            video = VideoFileClip(file_path)
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            resized_video = video.resize(newsize=(width, height))
            output_path = os.path.splitext(file_path)[0] + "_resized.mp4"
            resized_video.write_videofile(output_path)
            print(f"Video resized successfully: {output_path}")
        except Exception as e:
            print(f"Error resizing video: {e}")

    elif choice == "5":
        try:
            video = VideoFileClip(file_path)
            text = input("Enter text to add to video: ")
            fontsize = int(input("Enter font size: "))
            color = input("Enter text color (e.g., 'white', 'red'): ")
            text_clip = TextClip(text, fontsize=fontsize, color=color)
            text_clip = text_clip.set_position('center').set_duration(video.duration)
            final_video = CompositeVideoClip([video, text_clip])
            output_path = os.path.splitext(file_path)[0] + "_text_added.mp4"
            final_video.write_videofile(output_path)
            print(f"Text added successfully: {output_path}")
        except Exception as e:
            print(f"Error adding text to video: {e}")

    elif choice == "6":
        try:
            video = VideoFileClip(file_path)
            speed_factor = float(input("Enter speed factor (e.g., 2 for double speed, 0.5 for half speed): "))
            sped_up_video = video.fx(vfx.speedx, speed_factor)
            output_path = os.path.splitext(file_path)[0] + "_speed_changed.mp4"
            sped_up_video.write_videofile(output_path)
            print(f"Video speed changed successfully: {output_path}")
        except Exception as e:
            print(f"Error changing video speed: {e}")

    elif choice == "7":
        try:
            video = VideoFileClip(file_path)
            fade_duration = float(input("Enter fade-in duration in seconds: "))
            faded_video = video.fx(vfx.fadein, fade_duration)
            output_path = os.path.splitext(file_path)[0] + "_fade_in.mp4"
            faded_video.write_videofile(output_path)
            print(f"Fade-in effect applied successfully: {output_path}")
        except Exception as e:
            print(f"Error applying fade-in effect: {e}")

    elif choice == "8":
        try:
            video = VideoFileClip(file_path)
            music_path = input("Enter the path to the background music file: ")
            audio = AudioFileClip(music_path)
            final_video = video.set_audio(audio)
            output_path = os.path.splitext(file_path)[0] + "_with_music.mp4"
            final_video.write_videofile(output_path)
            print(f"Background music added successfully: {output_path}")
        except Exception as e:
            print(f"Error adding background music: {e}")

    elif choice == "9":
        try:
            video = VideoFileClip(file_path)
            start_time = float(input("Enter start time for trimming (in seconds): "))
            end_time = float(input("Enter end time for trimming (in seconds): "))
            trimmed_video = video.subclip(start_time, end_time)
            output_path = os.path.splitext(file_path)[0] + "_trimmed.mp4"
            trimmed_video.write_videofile(output_path)
            print(f"Video trimmed successfully: {output_path}")
        except Exception as e:
            print(f"Error trimming video: {e}")

    elif choice == "10":
        try:
            video = VideoFileClip(file_path)
            rotation_angle = int(input("Enter rotation angle (90, 180, 270): "))
            rotated_video = video.rotate(rotation_angle)
            output_path = os.path.splitext(file_path)[0] + "_rotated.mp4"
            rotated_video.write_videofile(output_path)
            print(f"Video rotated successfully: {output_path}")
        except Exception as e:
            print(f"Error rotating video: {e}")

    elif choice == "11":
        try:
            video = VideoFileClip(file_path)
            fade_duration = float(input("Enter fade-out duration in seconds: "))
            faded_video = video.fx(vfx.fadeout, fade_duration)
            output_path = os.path.splitext(file_path)[0] + "_fade_out.mp4"
            faded_video.write_videofile(output_path)
            print(f"Fade-out effect applied successfully: {output_path}")
        except Exception as e:
            print(f"Error applying fade-out effect: {e}")

    else:
        print("Invalid option selected.")

def handle_video(file_path):
    video_operations(file_path)
