from src.ProcessResultsHTML import process_results
from src.VideoProcessor import process_video

if __name__ == "__main__":
    input_video_path = "./assets/videos/video1.mp4"  # Replace with your video file path
    output_video_path = "./cache/videos/output/output_video.mp4"  # Replace with desired output path
    process_video(input_video_path, output_video_path)
    process_results("./cache/videos/","./cache/","resutls_v.html")
