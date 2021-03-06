import requests
from lxml import etree
import re
import os
Cookie = input("请输入Cookie:")

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
     "Cookie":Cookie,
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

pingjiao_url = 'http://218.29.109.240/eams/quality/stdEvaluate.action'

# 请求评教主页，获得老师与课程id相关字符串
resp = requests.get(pingjiao_url,headers=headers)

html = etree.HTML(resp.text)

# 解析获得老师与课程id列表
lesson_teacher_id = html.xpath("//tbody//a/@href")

submit_url ='http://218.29.109.240/eams/quality/stdEvaluate!finishAnswer.action'


for i in lesson_teacher_id:

    pattern = re.compile(r'\d+')

    # id_list为一个列表，包含两项，第一项是课程id,第二项是老师id
    id_list = pattern.findall(i)

    # 如果id_list长度为2，则说明未对此老师进行评教
    if len(id_list)==2:

        submit_data = {
            "teacher.id": id_list[1],
            "semester.id": "37",
            "evaluationLesson.id": id_list[0],
            "result1_0.questionName": "教师能合理利用优质教学资源，备课充分，认真组织教学，各环节安排合理，教学有序，辅导答疑、作业批改及时有效",
            "result1_0.content": "4",
            "result1_0.score": "18.000000000000004",
            "result1_1.questionName": "线上教学资源齐备（包含课程提纲、教学课件、视频、作业、参考资料等），达到了既定的课程学习目标，使学生能充分利用线上教学资源去学习本课程",
            "result1_1.content": "3",
            "result1_1.score": "8.000000000000002",
            "result1_2.questionName": "教学内容科学充实，逻辑性强，重点、难点突出。具有较丰富的观点、视角、深度和广度",
            "result1_2.content": "5",
            "result1_2.score": "10",
            "result1_3.questionName": "教师对本课程的学习目标和要求阐述清楚，课程考核标准明确",
            "result1_3.content": "4",
            "result1_3.score": "9.000000000000002",
            "result1_4.questionName": "教师结合网络教学特点，精心设计教学活动，灵活运用新媒体手段与学生进行有效沟通",
            "result1_4.content": "5",
            "result1_4.score": "15",
            "result1_5.questionName": "注重师生互动，有效组织学习活动促进师生、生生之间进行资源共享、问题交流和协作学习，培养学生的学习主动意识和创新意识",
            "result1_5.content": "3",
            "result1_5.score": "12",
            "result1_6.questionName": "掌握了这门课程的知识、技能并产生了浓厚的兴趣，收获很大且愿意深入学习",
            "result1_6.content": "4",
            "result1_6.score": "9.000000000000002",
            "result1_7.questionName": "该教师在本课程中的在线教学表现优秀，对学生的学习提供了较好的远程协助，愿意把该教师推荐给其他同学",
            "result1_7.content": "4",
            "result1_7.score": "9.000000000000002",
            "result2_0.questionName": "你对教师或课程的意见和建议",
            "result2_0.content": "比较满意",
            "result1Num": "8",
            "result2Num": "1"
        }

        r = requests.post(submit_url,data=submit_data,headers=headers)


        if r.status_code == 200:
            # print(ss1[i] + "-----" + ss2[i] + "------" + ss3[i] + "-----" + "评价完成！！")
            print('评价完成')

print("所有老师皆已评价完成，请在评教页面刷新查看。")

os.system('pause')





