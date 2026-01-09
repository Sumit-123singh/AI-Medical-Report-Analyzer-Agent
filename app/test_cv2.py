import cv2

img = cv2.imread(
    r"C:\Users\hp\OneDrive\Desktop\AI medical report analyzer agent\app\samples\sample_report.jpg",
    cv2.IMREAD_COLOR
)

print("OpenCV image loaded:", img is not None)
