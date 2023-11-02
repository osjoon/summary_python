import numpy as np
import cv2
import time

folder_path = "C:\\BIG_DATA_\\Opencv\\TF_waste\\can\\" # 사진 파일들이 있는 폴더 경로

for i in range(181,205):
    image = cv2.imread(folder_path + f'can{i}.jpg')  # 이미지 불러오기
    height, width, _ = image.shape
    # print(height, width)
    if 128 <= i <= 136:     # 예외 범위
        crop_width = 1080
        crop_height = 1080
    elif 138 <= i <= 140:     # 예외 범위
        crop_width = 1080
        crop_height = 1080
    else:
        crop_width = 1080
        crop_height = 1080

        # 중앙 좌표 계산
        center_x = width // 2
        center_y = height // 2

        # 중앙 좌표를 기준으로 크롭할 영역 계산
        x1 = center_x - crop_width // 2
        x2 = center_x + crop_width // 2
        y1 = center_y - crop_height // 2
        y2 = center_y + crop_height // 2

        # 이미지를 중앙 기준으로 크롭
        cropped_image = image[y1:y2, x1:x2]
        print(cropped_image)
        # 크롭된 이미지를 저장하거나 표시
        cv2.imshow(f'img{i}', cropped_image)
        cv2.imwrite(folder_path+f'can{i}.jpg', cropped_image)  # 크롭된 이미지를 파일로 저장
        cv2.waitKey()
        cv2.destroyAllWindows()
        if i > 206 :
            break




