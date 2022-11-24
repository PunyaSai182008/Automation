import cv2
import time
import random
import dropbox
from dropbox.files import WriteMode

start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)
    video_capture_object = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = video_capture_object.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
        return img_name
    print("Snapshot taken!!")

    video_capture_object.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.BTpf2oEEGWLl4Gm6S1tBpb-xtNCciP-DNi99gSnQmVCG4A5SOpRwv5xRartkZpIxWTapWWs0CCVZ-rt2SuXufrGczxzJ1X3Z6UFF6SwRHyydzdMMT4ppPJ44N-1BNwQpAZd-wP0"
    file_from = img_name
    file_to = "/newfolder1/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
        print("File Uploaded")


def main():
    while (True):
        if ((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)


main()
