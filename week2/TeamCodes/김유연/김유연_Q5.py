# 220124

# Q5. 이전에 구현한 클래스에서 merge_list의 함수 동작을 변경해야합니다. 단순합계가 아닌 평균을 구하는 함수로 변경해보세요.
#  - 리스트의 데이터를 다루는 함수를 이용해서 구현해보세요.
# - 최종 평균을 구한 후 오름차순으로 정렬해주세요.

class ReadCSV():
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file_list = []

    def read_file(self):
        if not self.__file_list: # if ile list is empty
            with open(self.__file_path,"r") as my_file:
                contents = my_file.read()
            self.__file_list = [list(map(int, l.split(','))) for l in contents.split("\n")]
        return self.__file_list
        
    
    def merge_list(self):
        self.read_file()
        return sorted([sum(i)/len(i) for i in self.__file_list])


file_path = "./week2/data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())


# 출력
# [[73, 80, 75, 152], [93, 88, 93, 185], [89, 91, 90, 180], [96, 98, 100, 196], [73, 66, 70, 142], [53, 46, 55, 101], [69, 74, 77, 149], [47, 56, 60, 115], [87, 79, 90, 175], [79, 70, 88, 164], [69, 70, 73, 141], [70, 65, 74, 141], [93, 95, 91, 184], [79, 80, 73, 152], [70, 73, 78, 148], [93, 89, 96, 192], [78, 75, 68, 147], [81, 90, 93, 183], [88, 92, 86, 177], [78, 83, 77, 159], [82, 86, 90, 177], [86, 82, 89, 175], [78, 83, 85, 175], [76, 83, 71, 149], [96, 93, 95, 192]]
# [63.75, 69.5, 87.5, 87.75, 88.25, 92.0, 92.25, 92.25, 94.75, 95.0, 96.0, 99.25, 100.25, 105.25, 107.75, 108.0, 108.75, 110.75, 111.75, 112.5, 114.75, 115.75, 117.5, 119.0, 122.5]