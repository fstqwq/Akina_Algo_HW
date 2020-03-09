
from timeit import default_timer as timer

import random

def measure_alg(alg, *arguments):
    start = timer()
    x = alg(*arguments)
    end = timer()
    return end - start



def measure_ratio(alg, n):
    return measure_alg(alg, 2*n) / measure_alg(alg, n)




def random_n_bit(n):
    result = 0
    while n > 0:
        result = result * 2
        bit = random.randint(0,1)
        result = result + bit
        n = n-1
    return result

def multiply(a,b):
    return a * b



student_names = ["任云玮",\
                 "王洋鲲",\
                 "徐逸凡",\
                 "钱苏澄",\
                 "龚勋",\
                 "罗雅婷",\
                 "杨宁",\
                 "李照宇",\
                 "郭文轩",\
                 "王玉林",\
                 "蔡亚星",\
                 "陈伟哲",\
                 "陈宇轩",\
                 "邓伟信",\
                 "侯博涵",\
                 "姜卫邦",\
                 "金乐盛",\
                 "李泊宁",\
                 "李嘉森",\
                 "凌皓煜",\
                 "刘尔之",\
                 "刘珺琪",\
                 "刘韫聪",\
                 "卢宇欣",\
                 "陆晗",\
                 "毛潇涵",\
                 "苏起冬",\
                 "孙恩泽",\
                 "孙司宇",\
                 "汪伟杰",\
                 "杨孟天",\
                 "杨培铭",\
                 "余子涵",\
                 "曾比扬",\
                 "张芳源",\
                 "张文涛",\
                 "张芷萁",\
                 "赵寒烨",\
                 "赵智游",\
                 "赵孜铧",\
                 "郑文鑫"];



def random_student():
    return random.choice(student_names)

def random_students(k):
    array = student_names.copy()
    random.shuffle(array)
    return array[0:k]












