import cv2
import numpy as np
from src.ImageProcessors.ProcessImage import save_image_to_disk
from setup import DEBUG, CACHE

DETECTOR = cv2.SIFT_create()

class ImageOI:
    def __init__(self, name, image_path):
        self.name = name
        self.image = cv2.imread(image_path)
        self.path = image_path
        self.image = cv2.resize(self.image, (512, 512))

        # Preprocessing
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.blurred = cv2.GaussianBlur(self.image_gray, (5, 5), 0)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Adaptive color segmentation
        lower_orange = (10, 100, 100)
        upper_orange = (25, 255, 255)
        self.mask = cv2.inRange(self.hsv_image, lower_orange, upper_orange)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        self.mask = cv2.morphologyEx(self.mask, cv2.MORPH_CLOSE, kernel)

        # Keypoint detection
        self.keypoints, self.descriptors = DETECTOR.detectAndCompute(self.image, None)

    def save_all_(self, path=f"{CACHE}"):
        save_image_to_disk(f"{path}/GRAYSCALE", self.name, self.image_gray, True)
        save_image_to_disk(f"{path}/1ORIGINAL", self.name, self.image, True)
        save_image_to_disk(f"{path}/MASK", self.name, self.mask, True)
        save_image_to_disk(f"{path}/BLURRED", self.name, self.blurred, True)
        save_image_to_disk(f"{path}/HSV", self.name, self.hsv_image, True)

        imageWithKeyPoints = cv2.drawKeypoints(self.image_gray, self.keypoints, self.image)
        save_image_to_disk(f"{path}/KEYPOINTS/", self.name, imageWithKeyPoints, True)

    def match_with_object(self, OJB):
        # FLANN-based matcher
        flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
        matches = flann.knnMatch(OJB.descriptors, self.descriptors, k=2)

        # Apply ratio test
        self.good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                self.good.append(m)

        if len(self.good) < 4:  # At least 4 points are required for homography
            print("Not enough matches to compute homography.")
            return None

        # Extract matched keypoints
        src_pts = np.float32([OJB.keypoints[m.queryIdx].pt for m in self.good]).reshape(-1, 1, 2)
        dst_pts = np.float32([self.keypoints[m.trainIdx].pt for m in self.good]).reshape(-1, 1, 2)

        # Compute homography
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        if M is None:
            print("Homography computation failed.")
            return None

        # Transform points and draw bounding box
        try:
            h, w = OJB.image_gray.shape
            pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, M)

            # Draw bounding box
            self.image = cv2.polylines(self.image, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
        except cv2.error as e:
            print(f"Error during perspective transform: {e}")
            return None

        # Save matches visualization
        draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=mask.ravel().tolist(), flags=2)
        self.drawMatches = cv2.drawMatches(OJB.image, OJB.keypoints, self.image, self.keypoints, self.good, None, **draw_params)

        return self.image
