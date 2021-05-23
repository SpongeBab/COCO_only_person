import os

if __name__ == '__main__':
    train_images = '/home/xiaopeng/coco_only_person/images/train2017'
    valid_images = '/home/xiaopeng/coco_only_person/images/val2017'
    train_txt = 'train.txt'
    valid_txt = 'valid.txt'
    # dest2 = 'D:\\VS2019Project\\darknet_master\\darknet-master\\mydata\\VOCdevkit\\VOC2020\\ImageSets\\Main\\val.txt'
    file_list = os.listdir(valid_images)
    train_file = open(train_txt, 'a')
    valid_file = open(valid_txt, 'a')
    # val_file = open(dest2, 'a')
    for file_obj in file_list:
        file_path = os.path.join(valid_images, file_obj)

        file_name, file_extend = os.path.splitext(file_obj)
        print(file_name)
        file_num = int(file_name)
        valid_file.write(file_path + '\n')

        # if file_num != 0:
        #
        #     train_file.write(file_name + '\n')
        # else:
        #     # val_file.write(file_name + '\n')
        #     break
    # train_file.close()
    valid_file.close()
