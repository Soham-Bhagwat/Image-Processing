# Load opencv module
import cv2
from imageio import imread
import numpy as np


# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.
# The default resolutions
# are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object. The output is
# stored in 'output.avi' file.
out = cv2.VideoWriter('output.avi',
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      10, (frame_width,frame_height))



while(True):
    
    ret, frame1 = cap.read()
    ret, frame = cap.read()

    if ret:
        ret, frame1 = cap.read()
        red1 = frame1[..., 0]
        green1 = frame1[..., 1]
        blue1 = frame1[..., 2]

        gray1 = np.average(frame1, weights=[0.299, 0.587, 0.114], axis=2)
        #gray1 = gray1.astype(np.uint8)

        #data = imread(frame)
        red = frame[..., 0]
        green = frame[..., 1]
        blue = frame[..., 2]

        gray = np.average(frame, weights=[0.299, 0.587, 0.114], axis=2)
        #gray = gray.astype(np.uint8)

        
        diff = gray1 - gray
        diff = abs(diff)
        diff = diff.astype(np.uint8)
        # color to grayscale

        # Write the frame into the file 'output.avi'
        # out.write(frame)
        #print(frame.dtype)
        #print(frame.shape)

        # Display the resulting frame
        cv2.imshow('frame', diff)
        
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done,
# release the video capture and write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
