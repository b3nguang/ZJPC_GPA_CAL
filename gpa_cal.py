import pandas as pd

excel_file = '1.xlsx'
data = pd.read_excel(excel_file)

score_to_point = {
    '优秀': 4.00,
    '良好': 3.00,
    '中等': 2.00,
    '及格': 1.00,
    '不及格': 0.00
}

sum_xuefen = sum(data['学分'])

data['成绩'] = data['成绩'].apply(lambda x: score_to_point[x] if x in score_to_point else x)
data['成绩'] = pd.to_numeric(data['成绩'], errors='coerce')
list_gpa = []

for index, row in data.iterrows():
    if row['考核方式'] == '考试':
        grade = 4 - 3 * (100 - row['成绩']) ** 2 / 1600
        gpa = grade * row['学分']
        list_gpa.append(gpa)
        print(row['课程名称'], gpa)
    else:
        grade = row['成绩']
        gpa = grade * row['学分']
        print(row['课程名称'], gpa)
        list_gpa.append(gpa)

print(f'总课程绩点:{sum(list_gpa)}')
print(f'总课程学分:{sum_xuefen}')

ave_apt = sum(list_gpa) / sum_xuefen
print(f'平均绩点:{ave_apt}')
