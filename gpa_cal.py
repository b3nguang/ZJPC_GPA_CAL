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

data['成绩'] = data['成绩'].replace(score_to_point).apply(pd.to_numeric, errors='coerce')
list_gpa = []

for index, row in data.iterrows():
    if row['考核方式'] == '考试':
        grade = 4 - 3 * (100 - row['成绩']) ** 2 / 1600
        if row['成绩'] < 60:
            grade = 0
    else:
        grade = row['成绩']

    gpa = grade * row['学分']
    list_gpa.append(gpa)
    print(row['课程名称'], gpa)

sum_gpa = sum(list_gpa)
sum_xuefen = data['学分'].sum()

print(f'总课程绩点: {sum_gpa}')
print(f'总课程学分: {sum_xuefen}')

ave_apt = sum_gpa / sum_xuefen
print(f'平均绩点: {ave_apt}')
