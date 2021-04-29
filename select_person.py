import os
import shutil
import inspect


def select_person(source_label_path, output_label_path, source_images_path, output_images_path):
    if not os.path.exists(output_label_path):
        os.makedirs(output_label_path)
    if not os.path.exists(output_images_path):
        os.makedirs(output_images_path)
    for txt_file in os.listdir(source_label_path):
        # print(txt_file)
        # 得到了txt_file的集合
        txt_name, extension = os.path.splitext(txt_file)
        # print(txt_name)
        with open(os.path.join(source_label_path, txt_file), "r") as f:
            fb = f.readlines()
            for line in fb[:]:
                # line = line.strip() # 错误的,使用这句会将换行符 /n 去掉，使输出变为一行
                linelist = line.split(" ")
                first = linelist[0]
                # output_file = os.path.join(output_path, txt_file)
                if "0" == linelist[0]:
                    outfile = open(os.path.join(output_label_path, txt_file), "a+")   # w这种打开方式会每次打开都把以前的覆盖掉，使用a或者a+，追加写
                    outfile.write(line)
                    src = os.path.join(source_images_path, txt_name + ".jpg")
                    dst = os.path.join(output_images_path, txt_name + ".jpg")
                    shutil.copy(src, dst)
                    print("已完成", dst)


if __name__ == '__main__':
    source_labels = "/home/xiaopeng/coco/labels/train2017"
    output_labels = "/home/xiaopeng/coco_only_person/labels/train2017"
    source_images = "/home/xiaopeng/coco/images/train2017"
    output_images = "/home/xiaopeng/coco_only_person/images/train2017"
    select_person(source_labels, output_labels, source_images, output_images)
