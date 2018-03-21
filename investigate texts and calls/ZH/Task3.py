"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

def get_header(phone):
    header = ''
    if phone.startswith('(') and phone.count(')') == 1:
        header = phone[:phone.index(')')+1]
        # print('{} 是 固话，前缀是: {}'.format(phone,header))
    elif phone.count(' ') == 1 and (phone[0] == '7' or phone[0] == '8' or phone[0] == '9'):
        header = phone[:4]
        # print('{} 是 手机，前缀是: {}'.format(phone,header))
    elif phone.count(' ') == 0 and phone.count('(') == 0 and phone.count(')') == 0 and phone[:3] == '140':
        header = phone[:4]
        # print('{} 是 促销员电话，前缀是: {}'.format(phone,header))
    else:
        print('{} 是 异常号码，无法获取前缀'.format(phone))

    return header

def is_bangalore(phone):
    return phone.startswith('(080)')

def find_all_headers_bangalore():
    set_all_header = set()
    for call in calls:
        if is_bangalore(call[0]) == False: 
            continue
        
        header = get_header(call[1])
        if header != '':
            set_all_header.add(header)
    
    return set_all_header

def sort_header_list(set_headers):
    l = []
    for header in set_headers:
        l.append(header)
    
    l.sort()
    return l

def print_all_sorted_bangalore_phones():
    set_headers = find_all_headers_bangalore()
    sorted_headers = sort_header_list(set_headers)

    ret_txt = ''
    for header in sorted_headers:
        ret_txt = ret_txt + '\n' + header
    
    print('The numbers called by people in Bangalore have codes:{}'.format(ret_txt))

def print_percent_bangalore_to_bangalore():
    from_count = 0
    to_count = 0
    for call in calls:
        if is_bangalore(call[0]):
            from_count += 1
            if is_bangalore(call[1]):
                to_count += 1
    
    percent = round(float(to_count / from_count * 100),2)
    print('{} percent of calls from fixed lines in Bangalore are callsto other fixed lines in Bangalore.'.format(percent))
        
# get_header('1408409918')
# get_header('(080)49328664')
# get_header('78132 18081')
# get_header('(022)38214945')
# sorted_header_list = sort_header_list(find_all_headers_080())
# print(sorted_header_list)

print_all_sorted_bangalore_phones()
print_percent_bangalore_to_bangalore()