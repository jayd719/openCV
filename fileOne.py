import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect_and_draw_box(filename, model="yolov3-tiny", confidence=0.6):
    """Detects common objects on an image and creates a new image with bounding boxes.
    Args:
        filename (str): Filename of the image.
        model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
        confidence (float, optional): Desired confidence level. Defaults to 0.6.
    """
    # Images are stored under the images/ directory
    img_filepath = f'images/{filename}'
    # Read the image into a numpy array
    img = cv2.imread(img_filepath)
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
    # Print current image's filename
    print(f"========================nImage processed: {filename}n")
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}n")
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)
    # Save the image in the directory images_with_boxes
    cv2.imwrite(f'images_with_boxes/{filename}', output_image)


# detect_and_draw_box('image.png')








# open webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Could not open video")
    exit()
    

# loop through frames
while video.isOpened():

    # read frame from webcam 
    status, frame = video.read()

    if not status:
        break

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')

    print(bbox, label, conf)

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
video.release()
cv2.destroyAllWindows()        
    
    
    
    
# detect_and_draw_box('image.png')
