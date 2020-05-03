# import the necessary packages
import numpy as np
import cv2
import os
import os.path

#This function minimizes the visual overlap from multiple detections
def non_max_suppression_fast(boxes, overlapThresh):
	# if there are no boxes, return an empty list
	if len(boxes) == 0:
		return []
	# if the bounding boxes integers, convert them to floats --
	if boxes.dtype.kind == "i":
		boxes = boxes.astype("float")
	
	picked = []
	# grab the coordinates of the bounding boxes
	x1 = boxes[:,0]
	y1 = boxes[:,1]
	x2 = boxes[:,2]
	y2 = boxes[:,3]
	# compute the area of the bounding boxes and sort the bounding
	# boxes by the bottom-right y-coordinate of the bounding box
	area = (x2 - x1 + 1) * (y2 - y1 + 1)
	idxs = np.argsort(y2)
	# keep looping while some indexes still remain in the indexes
	# list
	while len(idxs) > 0:
		# grab the last index in the indexes list and add the
		# index value to the list of picked indexes
		last = len(idxs) - 1
		i = idxs[last]
		picked.append(i)
		# find the largest (x, y) coordinates for the start of
		# the bounding box and the smallest (x, y) coordinates
		# for the end of the bounding box
		xx1 = np.maximum(x1[i], x1[idxs[:last]])
		yy1 = np.maximum(y1[i], y1[idxs[:last]])
		xx2 = np.minimum(x2[i], x2[idxs[:last]])
		yy2 = np.minimum(y2[i], y2[idxs[:last]])
		# compute the width and height of the bounding box
		w = np.maximum(0, xx2 - xx1 + 1)
		h = np.maximum(0, yy2 - yy1 + 1)
		# compute the ratio of overlap
		overlap = (w * h) / area[idxs[:last]]
		# delete all indexes from the index list that have
		idxs = np.delete(idxs, np.concatenate(([last],
			np.where(overlap > overlapThresh)[0])))
	# return only the bounding boxes that were picked using the
	# integer data type
	return boxes[picked].astype("int")
if __name__ == "__main__":
    # Delete old output
    if os.path.isfile("output.AVI"):
        os.remove("output.AVI")
    # Define input video resolutions
    resX = 1280
    resY = 720
    # define text parameters
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 2
    fontColor              = (0,255,0)
    lineType               = 2
    
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor("hog.xml")
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cv2.startWindowThread()

    # open webcam video stream
    cap = cv2.VideoCapture("input.mp4")

    # the output will be written to output.avi
    out = cv2.VideoWriter(
        'output.avi',
        cv2.VideoWriter_fourcc(*'MJPG'),
        15.,
        (resX,resY))

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Resizing can give faster detection
        # Note that people must be >64x128 for defaultPeopleDetector
        frame = cv2.resize(frame, (resX, resY))
        # greyscale for faster detection
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame)
        
        # Remove some overlapping boxes
        boxes = non_max_suppression_fast(boxes, 0.8)
        
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        posX = []
        for (xA, yA, xB, yB) in boxes:
            if xA < xB:
                posX.append(xA)
            else:
                posX.append(xB)
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)
        if len(posX) > 0:
            if len([i for i in posX if i > 430]) > 0:
                cv2.putText(frame,'*Buzz right*', 
                    (850,700), 
                    font, 
                    fontScale,
                    fontColor,
                    lineType)
            if len([i for i in posX if i < 860]) > 0:
                cv2.putText(frame,'*Buzz left*', 
                    (50,700), 
                    font, 
                    fontScale,
                    fontColor,
                    lineType)          
        # Write the output video 
        out.write(frame.astype('uint8'))
        # Display the resulting frame
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    # and release the output
    out.release()
    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)
