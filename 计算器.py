import easygui,sys


def add(left_num, right_num):
    return float(left_num) + float(right_num)


def minus(left_num, right_num):
    return float(left_num) - float(right_num)


def multiplication(left_num, right_num):
    return float(left_num) * float(right_num)


def divide(left_num, right_num):
    return float(left_num) / float(right_num)


ops_list = [multiplication, divide, add, minus]


def calculate(Numbering_of_op):
    while '*/+-'[Numbering_of_op] in num_list:
        tmp = num_list.index('*/+-'[Numbering_of_op])
        tmp_num = ops_list[Numbering_of_op](num_list[tmp - 1], num_list[tmp + 1])
        del num_list[tmp - 1:tmp + 2]
        num_list.insert(tmp - 1, tmp_num)

def split_expression1(tmp_express):
    num_list = []
    a = 0
    for i in range(0, 4):
        if '+-*/'[i] in tmp_express and tmp_express != '+-*/'[i]:
            tmp_list = tmp_express.split('+-*/'[i])
            while a < len(tmp_list) * 2:
                if a % 2 == 0:
                    num_list.append(tmp_list[int(a / 2)])
                else:
                    num_list.append('+-*/'[i])
                a += 1
            if num_list[len(num_list) - 1] == '+-*/'[i]:
                num_list.pop()
            break
    else:
        num_list.append(tmp_express)
    return num_list


def split_expression2(before_list, after_list=[]):
    for i in before_list:
        if i in '+-*/':
            after_list.append(i)
        else:
            try:
                float(i)
                after_list.append(i)
            except:
                after_list.extend(split_expression1(i))
    return after_list

while 1:
    expression = easygui.enterbox(
        '- 加法符号+\n- 减法符号-\n- 乘法符号*\n- 除法符号/\n- 默认优先级 * > / > - > +\n将会给出计算结果\n\n输入quit退出\n\n请输入算式：')
    if expression == 'quit':
        sys.exit()
    try:
        for i in range(0, 4):
            exec(f"temp{i + 1} = {'+-*/'[i] in expression}")
        times = temp1 + temp2 + temp3 + temp4
        if times >= 1:
            num_list = split_expression1(expression)
            for i in range(1,times):
                num_list = split_expression2(num_list)
        for i in range(0, 4):
            calculate(i)
        if num_list[0] % 1 == 0:
            easygui.msgbox(int(num_list[0]))
        else:
            easygui.msgbox(num_list[0])
    except TypeError:
        easygui.msgbox('输入的算式有误，请重新输入')
