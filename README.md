# 爬虫实战
记录学习爬虫的过程
### 01 爬取一页贴吧的内容
涉及：re模块使用(findall)和csv文件写入
1. 半自动爬取，手动复制页面源代码，保存到tieba.txt文件中
2. 打开tieba.txt文件，用f.read()将读取的内容存储到一个字符串中
3. 正则表达式findall匹配楼层帖子的内容、发帖人名称、发帖时间
4. 将收集到的内容保存到csv文件中


### 02 利用requests模块发起网络请求
1. 明确网页请求的多种模式，如get/post
2. 格式 requests.get('网址').content.decode()  或者 requests.post('网址',data=data).content.decode()
3. decode函数的参数默认是utf-8,可以不填

### 03 多线程、搜索算法
1. 爬虫属于I/O密集型操作，使用多线程可以提高效率
2. 开启多线程的方式
1)导入库 `from multiprocessing.dummy import Pool`
2)定义函数fun，定义可迭代对象list
3)申请线程池pool = Pool(线程数量)
4)多线程工作result = pool.map(fun,list)
3. 搜索算法，广度优先还是深度优先，依据于具体的问题而定
