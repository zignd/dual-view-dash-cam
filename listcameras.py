import cv2
import os

def find_available_cameras(max_tests=10):
    available_cameras = []
    for index in range(max_tests):
        cap = cv2.VideoCapture(index, cv2.CAP_ANY)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()
    return available_cameras

cameras = find_available_cameras()
print("Available cameras:", cameras)

def list_cameras():
    base_path = "/sys/class/video4linux"
    cameras = []
    for video_dev in os.listdir(base_path):
        video_path = os.path.join(base_path, video_dev, "name")
        if os.path.exists(video_path):
            with open(video_path, 'r') as f:
                camera_name = f.read().strip()
            cameras.append((video_dev, camera_name))
    return cameras

cameras_by_name = list_cameras()
print("Available cameras by name:", cameras_by_name)