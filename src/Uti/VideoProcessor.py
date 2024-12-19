import cv2 as cv
from src.ImageProcessors.functions import invert_image, brighten_image
from src.Uti.ProcessResultsHTML import process_results



def process_video(input_path, output_path, display_window='Processed Frame'):
    brighten_value = 50
    try:
        # Load the video
        cap = cv.VideoCapture(input_path)
        if not cap.isOpened():
            raise ValueError(f"Error: Cannot open video at {input_path}")

        # Get video properties
        frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv.CAP_PROP_FPS))

        # Define codec and VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        # Process video frame by frame
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("End of video or cannot fetch the frame.")
                break

            # Process the frame (example: convert to grayscale and brighten)
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            processed_frame = brighten_image(gray_frame, brighten_value)

            # Display the processed frame
            cv.imshow(display_window, processed_frame)

            # Convert grayscale back to BGR for saving
            bgr_frame = cv.cvtColor(processed_frame, cv.COLOR_GRAY2BGR)
            out.write(bgr_frame)

            # Exit on 'q' key press
            if cv.waitKey(10) & 0xFF == ord('q'):
                print("Processing interrupted by user.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Release resources
        cap.release()
        out.release()
        cv.destroyAllWindows()
        print("Resources released and application closed.")


