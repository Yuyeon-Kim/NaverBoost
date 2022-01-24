#시험 결과에 대한 csv 데이터 파일을 이용하여 데이터 처리하기
#파일 입출력을 이용해 파일 데이터를 리스트로 만들기
#hint:  파일 입출력에 사용하는 open 함수를 이용해 CSV 파일 내부의 데이터를 읽어보세요

#파일의 경로를 file_path로 설정
#ex) file_path = "./data-01-test-score.csv"



import csv

# file_path = "data-01-test-score.csv"

# def read_file(file_path):

#     def ReadCSV():
#         with open(file_path, "r") as f:
#             csv_data = csv.reader(f)
#             for row in csv_data:
#                 print(row)

# read_csv = ReadCSV(file_path)
# print(read_csv.read_file())


f = open("week2/data-01-test-score.csv", "r")
csv_data = csv.reader(f)
for row in csv_data:
    print(row)
f.close
