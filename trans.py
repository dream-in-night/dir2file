import os
import cv2
import numpy as np
path = "D:\\pics\\dilireba"
ids = 0
def my_cv_imread(filepath):
    # 使用imdecode函数进行读取
    img = cv2.imdecode(np.fromfile(filepath,dtype=np.uint8),-1)
    return img
def trans(path,ids):
	ids_ = ids
	dirs = os.listdir(path)
	for file in dirs:
		paths = os.path.join(path,file)
		print("paths:",paths)
		if not os.path.isdir(paths) and 'jpg' in str(paths)[-10:]:
			paths = paths.replace('\\','\\\\')
			print(paths)
			im = my_cv_imread(paths)
			if str(im) == "None":
				continue
			# print(im)
			im = cv2.resize(im,(512,512))
			cv2.imwrite("D:\\dili\\"+str(ids_)+'.jpg',im)
			ids_ += 1
			# print(ids_)
			# print('=======')
		if os.path.isdir(paths):
			trans(paths,ids)
			ids += 1
			# print('+++++++')
trans(path,ids)
# im = my_cv_imread("D:\\pics\\dilireba\\亮片鱼尾裙美艳动人写真图片\\1.jpg")
# print(str(im)==)
# im = cv2.resize(im,(512,512))