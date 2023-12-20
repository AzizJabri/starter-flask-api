from moviepy.editor import *
import boto3
s3 = boto3.client('s3')

class VideoGenerator:
    def create_reel_with_day_name(day_number, template_path):
        template_video = VideoFileClip(template_path)
        
        # Create a text clip for day number
        day_text = f"{day_number} DAYS"
        txt_clip_day = TextClip(day_text, fontsize=150, color='white', font='Arial-Bold', method='caption', stroke_color='black', stroke_width=3)

        # Create a text clip for additional text
        additional_text = "UNTIL GTA VI RELEASES"
        txt_clip_additional = TextClip(additional_text, fontsize=70, color='white', font='Arial-Bold',stroke_color='black', stroke_width=3 )

        # Position text clips
        txt_clip_day = txt_clip_day.set_position(('center', 550)).set_duration(template_video.duration)
        txt_clip_additional = txt_clip_additional.set_position(('center', 950)).set_duration(template_video.duration)

        # Composite text clips onto the template clip
        final_clip = CompositeVideoClip([template_video, txt_clip_day, txt_clip_additional])

        # Export the final reel
        output_path = f"reel_day_{day_number}.mp4"
        final_clip.write_videofile(output_path, codec='libx264', fps=24)

        return output_path

    def generate_1_frame(day_number, template_path):
        # Open the template image or video
        template_video = VideoFileClip(template_path)
        
        # Create a text clip for day number
        day_text = f"{day_number} DAYS"
        txt_clip_day = TextClip(day_text, fontsize=150, color='white', font='Arial-Bold', method='caption')

        # Create a text clip for additional text
        additional_text = "UNTIL GTA VI RELEASES"
        txt_clip_additional = TextClip(additional_text, fontsize=70, color='white', font='Arial-Bold')

        # Position text clips
        txt_clip_day = txt_clip_day.set_position(('center', 500)).set_duration(template_video.duration)
        txt_clip_additional = txt_clip_additional.set_position(('center', 900)).set_duration(template_video.duration)

        # Composite text clips onto the template clip
        final_clip = CompositeVideoClip([template_video, txt_clip_day, txt_clip_additional])

        # Export the frame as an image
        output_path = f"frame_day_{day_number}.png"
        final_clip.save_frame(output_path, t=0)  # t=0 to save the frame at the beginning (time=0)

        return output_path

