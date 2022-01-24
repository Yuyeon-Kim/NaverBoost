# 220124

# Q4. 우리는 방금 CSV 파일을 읽는 함수를 구현해보았습니다. 하지만 이를 조금 더 효율적으로 사용하기 위해서 클래스로 구성을 진행하려고 합니다. 방금 구현한 함수를 포함한 클래스를 구현해보세요.
#  - merge list를 이용해 리스트 내 데이터의 합을 출력해보세요.
#  - 데이터를 합치기 전 데이터의 자료형을 변경해보세요.

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path,"r") as my_file:
            contents = my_file.read()
        self.file_list = [list(map(int, l.split(','))) for l in contents.split("\n")]
        return self.file_list
    
    def merge_list(self):
        return [sum(i) for i in self.file_list]


file_path = "./week2/data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())