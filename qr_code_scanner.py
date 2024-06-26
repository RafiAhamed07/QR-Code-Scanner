import tkinter.messagebox as tkmsg
import webbrowser as wb

import cv2 as cv
import pytesseract
import pyzbar.pyzbar as bar

# Show instruction message
tkmsg.showinfo(title="Instructions", message="Press 'q' to quit the QR code scanner.")

# Open video capture (adjust index as per your camera device)
cam = cv.VideoCapture(1)

# Check if the camera is opened successfully
if not cam.isOpened():
    print("Error: Could not open video capture device.")
    exit()

while True:
    # Read frame from the camera
    ret, frame = cam.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Resize frame for OCR processing
    resized_frame = cv.resize(frame, (400, 400))
    h, w, c = resized_frame.shape

    # Perform OCR on the resized frame
    box = pytesseract.image_to_boxes(resized_frame)

    # Draw bounding boxes and text from OCR
    for b in box.splitlines():
        b = b.split()
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv.rectangle(resized_frame, (x, h - y), (w, h - h), (0, 0, 255), 1)
        cv.putText(resized_frame, b[0], (x - 5, h - y - 40), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    # Display OCR processed frame
    cv.imshow('QR code and OCR', resized_frame)

    # Detect QR codes in the original frame
    decoded_objs = bar.decode(frame)
    for obj in decoded_objs:
        if obj.data:
            qr_data = obj.data.decode('utf-8')
            print(f'Detected QR code: {qr_data}')
            wb.open(qr_data)  # Open QR code URL in a web browser

            # # Release camera and close OpenCV windows
            cam.release()
            cv.destroyAllWindows()
            exit()

    # Display QR code detected frame
    cv.imshow('QR code and OCR', frame)

    # Check for 'q' key press to quit
    key = cv.waitKey(1)
    if key == ord('q'):
        break

# Release the capture and close any OpenCV windows
cam.release()
cv.destroyAllWindows()
