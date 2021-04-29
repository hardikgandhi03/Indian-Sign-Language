import cv2
import os
import string

if not os.path.exists("dataset-alpha"):
    os.makedirs("dataset-alpha")
if not os.path.exists("dataset-alpha/train"):
    os.makedirs("dataset-alpha/train")
if not os.path.exists("dataset-alpha/test"):
    os.makedirs("dataset-alpha/test")

for i in string.ascii_uppercase:
    if not os.path.exists("dataset-alpha/train/" + str(i)):
        os.makedirs("dataset-alpha/train/" + str(i))
    if not os.path.exists("dataset-alpha/test/" + str(i)):
        os.makedirs("dataset-alpha/test/" + str(i))

mode = 'train'
folder = 'dataset-alpha/'+mode+'/'
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    no_of_img = {
        'a': len(os.listdir(folder + "/A")),
        'b': len(os.listdir(folder + "/B")),
        'c': len(os.listdir(folder + "/C")),
        'd': len(os.listdir(folder + "/D")),
        'e': len(os.listdir(folder + "/E")),
        'f': len(os.listdir(folder + "/F")),
        'g': len(os.listdir(folder + "/G")),
        'h': len(os.listdir(folder + "/H")),
        'i': len(os.listdir(folder + "/I")),
        'j': len(os.listdir(folder + "/J")),
        'k': len(os.listdir(folder + "/K")),
        'l': len(os.listdir(folder + "/L")),
        'm': len(os.listdir(folder + "/M")),
        'n': len(os.listdir(folder + "/N")),
        'o': len(os.listdir(folder + "/O")),
        'p': len(os.listdir(folder + "/P")),
        'q': len(os.listdir(folder + "/Q")),
        'r': len(os.listdir(folder + "/R")),
        's': len(os.listdir(folder + "/S")),
        't': len(os.listdir(folder + "/T")),
        'u': len(os.listdir(folder + "/U")),
        'v': len(os.listdir(folder + "/V")),
        'w': len(os.listdir(folder + "/W")),
        'x': len(os.listdir(folder + "/X")),
        'y': len(os.listdir(folder + "/Y")),
        'z': len(os.listdir(folder + "/Z")),


    }
    # cv2.putText(frame, "A: "+str(no_of_img['a']), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    # cv2.putText(frame, "B: "+str(no_of_img['b']), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    # cv2.putText(frame, "C: "+str(no_of_img['c']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    # cv2.putText(frame, "D: " + str(no_of_img['d']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "E: " + str(no_of_img['e']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "F: " + str(no_of_img['f']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "G: " + str(no_of_img['g']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "H: " + str(no_of_img['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "I: " + str(no_of_img['i']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "J: " + str(no_of_img['j']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "K: " + str(no_of_img['k']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "L: " + str(no_of_img['l']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "M: " + str(no_of_img['m']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "N: " + str(no_of_img['n']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "O: " + str(no_of_img['o']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "P: " + str(no_of_img['p']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Q: " + str(no_of_img['q']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "R: " + str(no_of_img['r']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "S: " + str(no_of_img['s']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "T: " + str(no_of_img['t']), (10, 410), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "U: " + str(no_of_img['u']), (10, 430), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "V: " + str(no_of_img['v']), (10, 450), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "W: " + str(no_of_img['w']), (10, 470), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "X: " + str(no_of_img['x']), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Y: " + str(no_of_img['y']), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Z: " + str(no_of_img['z']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    # print(frame.shape)
    x1 = int(0.5*frame.shape[1])
    x2 = frame.shape[1]-10
    y1 = 10
    y2 = int(0.5 * frame.shape[1])
    # print("{},{},{},{}".format(x1,y1,x2,y2)) Ans:- 320,10,630,320
    cv2.rectangle(frame,(319,9),(620+1,309),(0,255,0),1)
    roi=frame[10:300,320:620]

    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gaussblur = cv2.GaussianBlur(gray,(5,5),3)
    smallthres = cv2.adaptiveThreshold(gaussblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,2.8)
    ret, final_image = cv2.threshold(smallthres, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    final_image = cv2.resize(final_image, (300, 300))
    cv2.imshow("BW", final_image)

    interrupt = cv2.waitKey(1)
    if interrupt == ord('a'):
        cv2.imwrite(folder + 'A/' + str(no_of_img['a']) + '.jpg', final_image)
    if interrupt == ord('b'):
        cv2.imwrite(folder + 'B/' + str(no_of_img['b']) + '.jpg', final_image)
    if interrupt == ord('c'):
        cv2.imwrite(folder + 'C/' + str(no_of_img['c']) + '.jpg', final_image)
    if interrupt == ord('d'):
        cv2.imwrite(folder +'D/'+str(no_of_img['d'])+'.jpg', final_image)
    if interrupt == ord('e'):
        cv2.imwrite(folder + 'E/' + str(no_of_img['e']) + '.jpg', final_image)
    if interrupt == ord('f'):
        cv2.imwrite(folder + 'F/' + str(no_of_img['f']) + '.jpg', final_image)
    if interrupt == ord('g'):
        cv2.imwrite(folder +'G/'+str(no_of_img['g'])+'.jpg', final_image)
    if interrupt == ord('h'):
        cv2.imwrite(folder + 'H/' + str(no_of_img['h']) + '.jpg', final_image)
    if interrupt == ord('i'):
        cv2.imwrite(folder + 'I/' + str(no_of_img['i']) + '.jpg', final_image)
    if interrupt == ord('j'):
        cv2.imwrite(folder + 'J/' + str(no_of_img['j']) + '.jpg', final_image)
    if interrupt == ord('k'):
        cv2.imwrite(folder + 'K/' + str(no_of_img['k']) + '.jpg', final_image)
    if interrupt == ord('l'):
        cv2.imwrite(folder + 'L/' + str(no_of_img['l']) + '.jpg', final_image)
    if interrupt == ord('m'):
        cv2.imwrite(folder + 'M/' + str(no_of_img['m']) + '.jpg', final_image)
    if interrupt == ord('n'):
        cv2.imwrite(folder +'N/'+str(no_of_img['n'])+'.jpg', final_image)
    if interrupt == ord('o'):
        cv2.imwrite(folder + 'O/' + str(no_of_img['o']) + '.jpg', final_image)
    if interrupt == ord('p'):
        cv2.imwrite(folder + 'P/' + str(no_of_img['p']) + '.jpg', final_image)
    if interrupt == ord('Q'):
        cv2.imwrite(folder +'Q/'+str(no_of_img['q'])+'.jpg', final_image)
    if interrupt == ord('r'):
        cv2.imwrite(folder + 'R/' + str(no_of_img['r']) + '.jpg', final_image)
    if interrupt == ord('s'):
        cv2.imwrite(folder + 'S/' + str(no_of_img['s']) + '.jpg', final_image)
    if interrupt == ord('t'):
        cv2.imwrite(folder + 'T/' + str(no_of_img['t']) + '.jpg', final_image)
    if interrupt == ord('u'):
        cv2.imwrite(folder + 'U/' + str(no_of_img['u']) + '.jpg', final_image)
    if interrupt == ord('v'):
        cv2.imwrite(folder + 'V/' + str(no_of_img['v']) + '.jpg', final_image)
    if interrupt == ord('w'):
        cv2.imwrite(folder + 'W/' + str(no_of_img['w']) + '.jpg', final_image)
    if interrupt == ord('x'):
        cv2.imwrite(folder +'X/'+str(no_of_img['x'])+'.jpg', final_image)
    if interrupt == ord('y'):
        cv2.imwrite(folder + 'Y/' + str(no_of_img['y']) + '.jpg', final_image)
    if interrupt == ord('z'):
        cv2.imwrite(folder + 'Z/' + str(no_of_img['z']) + '.jpg', final_image)

    if interrupt == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()