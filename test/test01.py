import requests
import json
from openpyxl import workbook  # 写入Excel表所用

url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=android&for_mobile=1&start=0&count=50&loc_id=108288&_=1596118703439"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
    "Referer": "https://m.douban.com/tv/chinese"
}
path = "E:/testData/testPY/"
response = requests.get(url, headers=headers)
json_str = response.content.decode()
files = json.loads(json_str)
maxValue = 0  # 最高分
highCount = 0  # 大于8分的是高分
Chinese = []
ChineseXG = []
ChineseTW = []
wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
# 往表中写入标题行,以列表形式写入！
ws.append(['电影名', '年份', '概述', '评分', '最近评论'])
for i in range(50):
    title = files["subject_collection_items"][i]["title"]
    year = files["subject_collection_items"][i]["year"]
    info = files["subject_collection_items"][i]["info"]
    rating = files["subject_collection_items"][i]["rating"]
    recommend_comment = files["subject_collection_items"][i]["recommend_comment"]
    if None is rating:
        ratingValue = 0
    else:
        ratingValue = rating['value']
    if maxValue <= ratingValue:
        maxValue = ratingValue
    if info.find("中国大陆") >= 0:
        Chinese.append(title + ',')
    if info.find("中国香港") >= 0:
        ChineseXG.append(title + ',')
    if info.find("中国台湾") >= 0:
        ChineseTW.append(title + ',')
    if ratingValue >= 8:
        highCount = highCount + 1

    ws.append([title, year, info, ratingValue, recommend_comment])
    wb.save('E:/testData/testPY/chinese.xlsx')
    img = files["subject_collection_items"][i]["cover"]["url"]
    img1 = requests.get(img, headers=headers)
    with open(path + img[-9:], "wb")as a:
        a.write(img1.content)
        a.close()
with open("E:/testData/testPY/统计.txt", "a", encoding="utf-8") as f:
    f.write("最近50个中国电视剧中，最高分：" + str(maxValue)+ "\n")
    print("最近50个中国电视剧中，最高分：" + str(maxValue) + "\n")
    f.write("最近50个中国电视剧中，优秀电视剧（大于8分）的个数为" + str(highCount) + "\n")
    print("最近50个中国电视剧中，最高分位" + str(highCount) + "\n")
    f.write("大陆电视剧有：")
    print("大陆电视剧有：")
    for i in range(len(Chinese)):
        f.write(Chinese[i] + " ")
        print(Chinese[i] + " ")
    f.write("\n")
    print("\n")

    f.write("香港电视剧有：")
    print("香港电视剧有：")
    for i in range(len(ChineseXG)):
        f.write(ChineseXG[i] + " ")
        print(ChineseXG[i] + " ")
    print("\n")
    f.write("\n")

    f.write("台湾电视剧有：")
    print("台湾电视剧有：")
    for i in range(len(ChineseTW)):
        f.write(ChineseTW[i] + " ")
        print(ChineseTW[i] + " ")
    f.close()
