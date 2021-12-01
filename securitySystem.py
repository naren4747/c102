import cv2
import random
import time
import dropbox

startTime=time.time()

def takeSnapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        imgName="img"+str(number)+".jpg"
        cv2.imwrite(imgName,frame)
        result=False

    return imgName
    print("SnapShotTaken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgName):
    accessToken="i3NE5StZ-NkAAAAAAAAAAcAIPylCiDBtF9sx2oNUBScBSOUNT7WbGthqf1FfPcMj"
    file=imgName
    file_from=file
    file_to="/newfolder1/"+(imgName)
    dbx=dropbox.Dropbox(accessToken)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=10):
            name=takeSnapShot()
            uploadFile(name)

main()

