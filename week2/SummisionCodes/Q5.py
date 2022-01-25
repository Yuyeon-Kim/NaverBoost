# 220124

# Q5. 이전에 구현한 클래스에서 merge_list의 함수 동작을 변경해야합니다. 단순합계가 아닌 평균을 구하는 함수로 변경해보세요.
#  - 리스트의 데이터를 다루는 함수를 이용해서 구현해보세요.
#  - 최종 평균을 구한 후 오름차순으로 정렬해주세요.

class ReadCSV():
    def __init__(self, file_path): # ReadCSV의 생성자, file_path 를 매개 변수로 받음
        self.__file_path = file_path # private 매개변수 __file_path에 초기값 저장
        self.__file_list = [] # private 매개변수 __file_list 초기화, 이후 파일을 리스트 형태로 저장할 매개변수

    def read_file(self):
        if not self.__file_list: # 파일 리스트가 비어있어서 처음 파일을 읽는다면
            with open(self.__file_path,"r") as my_file: # 파일을 읽기모드로 열어서 my_file이라 별명붙임
                contents = my_file.read()  # 파일의 모든 내용을 str 자료형으로 저장
            self.__file_list = [list(map(int, l.split(','))) for l in contents.split("\n")] # 줄나눔을 기준으로 split 후 컴마(,) 기준으로 split 후 map 함수를 사용해 형변환
        return self.__file_list # __file_list return
        
    def merge_list(self):
        return sorted([sum(i)/len(i) for i in self.read_file()]) # 각 행의 합계 / 원소 개수로 평균 구한 뒤 sorted 함수 사용해 오름차순 정렬

# 파일의 경로를 file_path로 설정
file_path = "./week2/data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.merge_list())

# 출력
# [63.75, 69.5, 87.5, 87.75, 88.25, 92.0, 92.25, 92.25, 94.75, 95.0, 96.0, 99.25, 100.25, 105.25, 107.75, 108.0, 108.75, 110.75, 111.75, 112.5, 114.75, 115.75, 117.5, 119.0, 122.5]