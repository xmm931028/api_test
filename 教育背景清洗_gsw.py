import pymysql
import re

# db_base = pymysql.connect(host='172.16.207.64',
#                       # port = 3306,
#                       # user='root',
#                       # password='V39EVHP8KGHIPPXW',
#                        database='data')

db_base = pymysql.connect(host='172.16.154.78',
                          port=3306,
                          user='root',
                          password='pyuKRr9NFpf3hLD2s',
                          database='data')

cursor = db_base.cursor()
sql_query1 = """\
SELECT *
FROM person_edu_experience
WHERE school_name REGEXP '[^（(]*[，,。、；;][^）)]*$'
"""
cursor.execute(sql_query1)
result = cursor.fetchall()
for i in result:  ####
    person_id = i[1]
    school_name = i[2]
    professional = i[3]
    degree = i[4]
    start_time = i[5]
    end_time = i[6]
    school_url = i[7]
    created_at = i[8]
    updated_at = i[9]
    replace_school = school_name.replace(',', '，').replace('(', '（').replace(')', '）').replace(r'\n', '，') \
        .replace('。', '，').replace(';', '，').replace('；', '，').replace('、', '，')
    split_school = re.split(r"，(?![^（]*\）)", replace_school)

    for school_name in split_school:
        try:
            if school_name == '':
                continue
            else:
                insert_query = "INSERT INTO person_edu_experience (person_id, school_name, professional,degree,start_time,end_time,school_url,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                person_id, school_name, professional, degree, start_time, end_time, school_url, created_at, updated_at)
                cursor.execute(insert_query, values)
        except pymysql.IntegrityError as e:
            print("重复数据，已跳过:", e)
            continue
print('1已完成教育背景分割插入完成')

# 把上面的插入完成后把原有数据删除
sql_query2 = "delete FROM person_edu_experience  WHERE school_name REGEXP '[^（(]*[，,。、；;][^）)]*$'"
cursor.execute(sql_query2)
print('2已完成括号外带有，、等值已删除')
sql_query3 = """DELETE FROM 
    person_edu_experience
WHERE 
    school_name LIKE '%师' 
    AND (school_name NOT LIKE '%大学%' or school_name NOT LIKE '%学院%');"""
cursor.execute(sql_query3)
print('3已完成，删除**师，不包含大学学院')
sql_query4 = """DELETE FROM 
    person_edu_experience
WHERE 
    school_name LIKE '%生' 
    AND (school_name NOT LIKE '%大学%' or school_name NOT LIKE '%学院%');"""
cursor.execute(sql_query4)
print('4已完成，删除**生，不包含大学学院')
sql_query5 = """\
select
    *,CONCAT(SUBSTRING_INDEX(school_name, '大学', 1),'大学')
from person_edu_experience
WHERE         
    school_name LIKE '%大学%系%';"""

cursor.execute(sql_query5)
result5 = cursor.fetchall()
for i in result5:  ####
    person_id = i[1]
    school_name = i[-1]
    professional = i[3]
    degree = i[4]
    start_time = i[5]
    end_time = i[6]
    school_url = i[7]
    created_at = i[8]
    updated_at = i[9]
    try:

        insert_query = "INSERT INTO person_edu_experience (person_id, school_name, professional,degree,start_time,end_time,school_url,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
        person_id, school_name, professional, degree, start_time, end_time, school_url, created_at, updated_at)
        cursor.execute(insert_query, values)
    except pymysql.IntegrityError as e:
        print("重复数据，已跳过:", e)
        continue
sql_query_d_5 = "delete from person_edu_experience WHERE school_name LIKE '%大学%系%'"
cursor.execute(sql_query_d_5)
print('5已完成，更新大学后含有系的')
sql_query6 = """select
*,CONCAT(SUBSTRING_INDEX(school_name, '学院', 1),'学院')
from
    person_edu_experience
WHERE       
     school_name LIKE '%学院%系%' and school_name  not like '%大学%系%';"""
cursor.execute(sql_query6)
result6 = cursor.fetchall()

for i in result6:  ####
    person_id = i[1]
    school_name = i[-1]
    professional = i[3]
    degree = i[4]
    start_time = i[5]
    end_time = i[6]
    school_url = i[7]
    created_at = i[8]
    updated_at = i[9]
    try:

        insert_query = "INSERT INTO person_edu_experience (person_id, school_name, professional,degree,start_time,end_time,school_url,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
        person_id, school_name, professional, degree, start_time, end_time, school_url, created_at, updated_at)
        cursor.execute(insert_query, values)
    except pymysql.IntegrityError as e:
        print("重复数据，已跳过:", e)
        continue
sql_query_d_6 = "delete from person_edu_experience WHERE school_name LIKE '%学院%系%' and school_name  not like '%大学%系%';"
cursor.execute(sql_query_d_6)
print('6已完成，更新学院后含有系的')
sql_query7 = """
DELETE FROM
    person_edu_experience
WHERE
         school_name = '本科' 
        OR school_name = '硕士' 
        OR school_name='博士'
        OR school_name='研究生';"""

cursor.execute(sql_query7)
print('7已完成，删除本科，硕士等的值')
db_base.commit()
cursor.close()
db_base.close()