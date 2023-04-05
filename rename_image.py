#=====================================================================
#===============Chuong trinh doi ten anh su dung python===============
#===============Luu Kien =============
#out_path = path_processed + "ID" + str(index) + "." + str(k) + ".png"

import os
import sys
import cv2

path_processed = "/home/vncssd/Desktop/RenameApp/PathOut/"#Path chua anh da xu li

in_path = "/home/vncssd/Desktop/RenameApp/image/"#path chua anh chua rename
k = 0
for index in os.listdir(in_path):
    folder_image_path = in_path + str(k)#str(index) + "/" + str(k) + "/"#+ "/image_detected"
    for image_name in os.listdir(folder_image_path):
        image_path = os.path.join(folder_image_path, image_name)
        image = cv2.imread(image_path)
        out_path = path_processed + "ID" + "." + str(index) + ".png"
        cv2.imwrite(out_path, image)
        k += 1
print 'Da doi ten thanh cong !'
   

