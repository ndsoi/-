import re
import csv

with open('tieba.txt','r',encoding='utf-8') as f:
    content = f.read()

lous = re.findall('l_post l_post_bright j_l_post clearfix(.*?)<ul class="p_props_tail props_appraise_wrap"></ul>',content,re.S)


num = 0
data = []
for every in lous:
    write_list = {}
    write_list['name']=  re.findall('class="p_author_name j_user_card".*?>(.*?)</a>',every,re.S)[0]

    write_list['content'] = re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)</div>',every,re.S)[0]

    write_list['time'] = re.findall('<span class="tail-info">(.*?)</span>',every,re.S)[2]
    data.append(write_list)


with open('result.csv','w',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['name','content','time'])
    writer.writeheader()
    writer.writerows(data)


   
