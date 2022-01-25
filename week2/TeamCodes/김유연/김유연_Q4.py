# 220124

# Q4. 우리는 방금 CSV 파일을 읽는 함수를 구현해보았습니다. 하지만 이를 조금 더 효율적으로 사용하기 위해서 클래스로 구성을 진행하려고 합니다. 방금 구현한 함수를 포함한 클래스를 구현해보세요.
#  - merge list를 이용해 리스트 내 데이터의 합을 출력해보세요.
#  - 데이터를 합치기 전 데이터의 자료형을 변경해보세요.

class ReadCSV():
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file_list = []

    def read_file(self):
        if not self.__file_list: # if file list is empty
            with open(self.__file_path,"r") as my_file:
                contents = my_file.read()
            self.__file_list = [list(map(int, l.split(','))) for l in contents.split("\n")]
        return self.__file_list
        
    def merge_list(self):
        self.read_file()
        return [sum(i) for i in self.__file_list]


file_path = "./week2/data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())

# 출력
# [[73, 80, 75, 152], [93, 88, 93, 185], [89, 91, 90, 180], [96, 98, 100, 196], [73, 66, 70, 142], [53, 46, 55, 101], [69, 74, 77, 149], [47, 56, 60, 115], [87, 79, 90, 175], [79, 70, 88, 164], [69, 70, 73, 141], [70, 65, 74, 141], [93, 95, 91, 184], [79, 80, 73, 152], [70, 73, 78, 148], [93, 89, 96, 192], [78, 75, 68, 147], [81, 90, 93, 183], [88, 92, 86, 177], [78, 83, 77, 159], [82, 86, 90, 177], [86, 82, 89, 175], [78, 83, 85, 175], [76, 83, 71, 149], [96, 93, 95, 192]]
# [380, 459, 450, 490, 351, 255, 369, 278, 431, 401, 353, 350, 463, 384, 369, 470, 368, 447, 443, 397, 435, 432, 421, 379, 476]