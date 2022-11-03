"""
Script to creat a CSV annotation files for all the images in a given folder
and given text file.
The text file here is TrainIJCNN2013/gt.txt, so the code is according to that.
"""

import cv2
import pandas as pd


def text_to_csv(dir_path):
    train_dir = f"{dir_path}/TrainIJCNN2013"
    txt_file_path = f"{train_dir}/gt.txt"
    csv_file_path = f"{dir_path}/signnames.csv"
    out_file_path = f"{dir_path}/all_annots.csv"

    # Class names.
    sign_names_df = pd.read_csv(csv_file_path)
    class_names = sign_names_df.SignName.tolist()

    with open(txt_file_path) as f:
        all_lines = f.readlines()
    f.close()

    all_lines = [line.split('\n')[0] for line in all_lines]

    file_name = []
    x_min = []
    y_min = []
    x_max = []
    y_max = []
    class_name = []
    width = []
    height = []

    for line in all_lines:
        all_elements = line.split(';')
        file_name.append(all_elements[0])
        x_min.append(all_elements[1])
        y_min.append(all_elements[2])
        x_max.append(all_elements[3])
        y_max.append(all_elements[4])
        class_name.append(class_names[int(all_elements[5])])
        image = cv2.imread(f'{train_dir}/{all_elements[0]}')
        img_height, img_width, _ = image.shape
        width.append(img_width)
        height.append(img_height)

    csv_file = pd.DataFrame(columns=[
        'file_name', 'width', 'height',
        'class_name', 'x_min', 'y_min', 'x_max', 'y_max'
    ])
    csv_file['file_name'] = file_name
    csv_file['x_min'] = x_min
    csv_file['x_max'] = x_max
    csv_file['y_min'] = y_min
    csv_file['y_max'] = y_max
    csv_file['class_name'] = class_name
    csv_file['width'] = width
    csv_file['height'] = height

    print(csv_file.head())
    csv_file.to_csv(out_file_path, index=False)


text_to_csv(dir_path="../../input")
