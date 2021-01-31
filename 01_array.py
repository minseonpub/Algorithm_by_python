#chapter5. 배열
# #연습1: 위의 2차원 배열에서 9, 8, 7 을 순서대로 출력해보기
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in reversed(data_list):  #역순 출력(reversed)
    print(i)

for j in range(2, -1, -1):
    print(data_list[2][j])

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

# 연습2: 위의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기
count =0
for i in dataset:
    for j in range(0, len(i)):
        if i[j] =='M': count=count+1
print(count)

count2 =0;
search = 'M'
for k in dataset:
    if k.count(search) != 0:
        count2 = count2 +k.count(search)
print(count2)
# list.count : 특정문자열이 포함된 개수
# if search in k: 이거 하면 하나라도 있음 체크

# range(stop): range(10)은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(start, stop): range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# range(start, stop, step): range(0, 20, 2)은 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# start, stop, step은 음수로 지정 가능


