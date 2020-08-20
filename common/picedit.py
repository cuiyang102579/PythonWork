#coding=utf-8
import os  #打开文件时需要
from PIL import Image

# 图片分辨率修改，只支持png

Start_path='D:\pic'
iphone5_width=200
iphone5_depth=200
list=os.listdir(Start_path)
print(list)
count=0
for pic in list:
    path=Start_path+'\\'+pic
    print (path)
    im=Image.open(path)
    w,h=im.size
    print (w,h)
    #
    if pic == '1.png' or  pic == '2.png' or pic == '3.png' or pic == '4.png':
        h_new = 1242
        w_new = 2208
        out = im.resize((h_new, w_new), Image.ANTIALIAS)
        out.save(path)
        count = count+1

    if pic == '200-200.png' :
        h_new = 200
        w_new = 200
        out = im.resize((w_new, h_new), Image.ANTIALIAS)
        out.save(path)
        #iphone 5的分辨率为1136*640，如果图片分辨率超过这个值，进行图片的等比例压缩
        count = count+1


    if pic == '310-280.png' :
        h_new = 310
        w_new = 280
        out = im.resize((h_new, w_new), Image.ANTIALIAS)
        out.save(path)
        count = count+1


    # if w!=iphone5_width or h!=iphone5_depth:
    #     print(pic)
    #     print("图片名称为"+pic+"图片被修改")
    #     h_new=350
    #     w_new=350
    #     count=count+1
    #     out = im.resize((w_new,h_new),Image.ANTIALIAS)
    #     new_pic=re.sub(pic[:-4],pic[:-4],pic)
    #     #print new_pic
    #     new_path=Start_path+new_pic
    #     out.save(new_path)

print('END')
count=str(count)
print("共有"+count+"张图片尺寸被修改")