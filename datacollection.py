import cv2
import numpy as np
import os
if not os.path.exists("dataset"):
    os.makedirs("dataset")
if not os.path.exists("dataset/train"):
    os.makedirs("dataset/train")
if not os.path.exists("dataset/test"):
    os.makedirs("dataset/test")

for i in range(10):
    if not os.path.exists("dataset/train/" + str(i)):
        os.makedirs("dataset/train/" + str(i))
    if not os.path.exists("dataset/test/" + str(i)):
        os.makedirs("dataset/test/" + str(i))

mode = 'train'
directory = 'dataset/'+mode+'/'
cap = cv2.VideoCapture(0)
#interrupt = -1
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    count = {
        'zero': len(os.listdir(directory + "0")),
        'one': len(os.listdir(directory + "1")),
        'two': len(os.listdir(directory + "2")),
        'three': len(os.listdir(directory + "3")),
        'four': len(os.listdir(directory + "4")),
        'five': len(os.listdir(directory + "5")),
        'six': len(os.listdir(directory + "6")),
        'seven': len(os.listdir(directory + "7")),
        'eight': len(os.listdir(directory + "8")),
        'nine': len(os.listdir(directory + "9")),

    }
    cv2.putText(frame, "Zero : "+str(count['zero']), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "One : "+str(count['one']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Two : "+str(count['two']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Three : "+str(count['three']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Four : "+str(count['four']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Five : "+str(count['five']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Six : "+str(count['six']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Seven : "+str(count['seven']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Eight : "+str(count['eight']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Nine : "+str(count['nine']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    # print(frame.shape)
    # x1 = int(0.5*frame.shape[1])
    # x2 = frame.shape[1]-10
    # y1 = 10
    # y2 = int(0.5 * frame.shape[1])
    # # print("{},{},{},{}".format(x1,y1,x2,y2)) Ans:- 320,10,630,320
    cv2.rectangle(frame,(320,10),(620,320),(0,255,0),1)
    roi=frame[10:320,320:620]
    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gaussblur = cv2.GaussianBlur(gray,(5,5),2)
    smallthres = cv2.adaptiveThreshold(gaussblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,2.8)
    ret, final_image = cv2.threshold(smallthres, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    final_image = cv2.resize(final_image, (300, 300))
    cv2.imshow("BW", final_image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    interrupt = cv2.waitKey(10)

    if interrupt == 27:  # esc key
        break
    if interrupt == ord('0'):
        cv2.imwrite('dataset/train/0/' + str(count['zero']) + '.jpg', final_image)
    if interrupt == ord('1'):
        cv2.imwrite(directory + '1/' + str(count['one']) + '.jpg', final_image)
    if interrupt == ord('2'):
        cv2.imwrite(directory + '2/' + str(count['two']) + '.jpg', final_image)
    if interrupt == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', final_image)
    if interrupt == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', final_image)
    if interrupt == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', final_image)
    if interrupt == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', final_image)
    if interrupt == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', final_image)
    if interrupt == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', final_image)
    if interrupt == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', final_image)

cap.release()
cv2.destroyAllWindows()
