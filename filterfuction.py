import os

folder_path = "Opencv\\TF_waste\\can" # 사진 파일들이 있는 폴더 경로
# new_path ="C:\\BIG_DATA_\\Opencv\\TF_waste\\Data\\can"
cnt=1
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        date_part1 = filename.split("_")[0]  # 재질 부분 추출
        date_part2 = filename.split("_")[1]  # 날짜 부분 추출
        date_part1.replace('KakaoTalk', 'can')

        new_filename = f"can{cnt}.jpg"  # 새로운 파일명 생성
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)  # 파일 이름 변경
        cnt+=1