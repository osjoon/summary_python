# --------------------------------------------------------------
# 수비드조리법 클래스
# 클래스명 : SousvideCooking                       # GUI 기능? 패키지? 쓰는 것
# 속성필드 : meat_temperatures
# 기능역할 : get_cooking_info(), add_cooking_info()
# --------------------------------------------------------------
# 검색 기록 경로 설정
DIR_PATH = "C:\\EXAM_4PYTHON\\DAY_09\\"
filename = DIR_PATH + "cookingdata.txt"

# 클래스 생성
class SousvideCooking:
    def __init__(self):
        # 저장된 수비드 조리법과 그 특성을 저장해놓음
        self.meat_temperatures = {
            '삼겹살': {'최적 온도': '70도', '최적 시간': '24h', '식감': '지방이 잘 녹아있음', '질감': '썰기 힘들정도로 부드러움'},
            '닭가슴살': {'최적 온도': '60도', '최적 시간': '1h', '식감': '매우 부드럽고 촉촉함', '질감': '수분감을 가지며 부드러움'},
            '소갈비': {'최적 온도': '75도', '최적 시간': '18h', '식감': '결대로 녹는 식감', '질감': '쫄깃하면서 부드러움'},
            '아롱사태': {'최적 온도': '73도', '최적 시간': '16h', '식감': '젤라틴화 된 힘줄이 고기와 씹힘', '질감': '부드럽고 쫄깃한'},
            '생선류': {'최적 온도': '60도', '최적 시간': '30m~1h', '식감': '촉촉하게 구워진 생선구이의 속살만 먹는듯함', '질감': '말랑부들'}
        }

    def get_cooking_info(self):
        while True:
            # protein_part로 수비드 조리할 부위를 입력받음 (q 입력시 종료)
            protein_part = input("단백질 식품 부위를 입력하세요 (나가기: q): ")
            if protein_part.lower() == 'q':
                break
            # protein_part가 meat_temperatures 안에 있는 부위라면 출력해주도록 함
            if protein_part in self.meat_temperatures:
                info = self.meat_temperatures[protein_part]
                print(f"최적 온도: {info['최적 온도']}")
                print(f"최적 시간: {info['최적 시간']}")
                print(f"식감: {info['식감']}")
                print(f"질감: {info['질감']}")
            else:
                print("해당 단백질 식품 부위의 정보를 찾을 수 없습니다.")

    # version 2 
    def add_cooking_info(self, protein_part, temperature, time, texture, tenderness):
        self.meat_temperatures[protein_part] = {'최적 온도': temperature, '최적 시간': time, '식감': texture, '질감': tenderness}

    # 입력받은 protein_part를 데이터로 남기는 함수
    def save_to_file(self, protein_part, info, filename):
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"단백질 식품 부위: {protein_part}\n")
            file.write(f"최적 온도: {info['최적 온도']}\n")
            file.write(f"최적 시간: {info['최적 시간']}\n")
            file.write(f"식감: {info['식감']}\n")
            file.write(f"질감: {info['질감']}\n\n")
        print("결과가 파일에 저장되었습니다.")
        

# --------------- 함수 호출 -------------------
sousvide = SousvideCooking()

sousvide.add_cooking_info('수비드수육', '70도', '4h', '식감: 씹는 맛있는 수육', '질감: 뻑뻑하지 않은 질감')

protein_part = input("단백질 식품 부위를 입력해주세요: ")

sousvide.save_to_file(protein_part, sousvide.meat_temperatures[protein_part], filename)

result = sousvide.get_cooking_info()
print(result)

