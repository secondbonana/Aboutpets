import openpyxl

# 한 건의 대화에 대한 정보를 담는 객체생성
class Conversation:
    # 질문, 응답 두 변수로 구성됨.
    def __init__(self, contentName, contentType, question, answer):
        self.contentName = contentName
        self.contentType = contentType
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"


# 데이터가 담긴 엑셀 파일을 열기.
wb = openpyxl.load_workbook(r'C:\Users\DK\Desktop\project\Dialogflow_chatbot/input.xlsx')


# 활성 시트를 얻는다.
ws = wb.active

conversations = []


# 시트 내에 존재하는 모든 대화 데이터를 객체로 담는다.
for a in ws.rows:
    b = Conversation(a[0].value, a[1].value, a[2].value, a[3].value)
    conversations.append(b)

wb.close()


# 모든 데이터를 출력합니다.
for c in conversations:
    print(str(c))

print('총', len(conversations), '개의 대화가 존재합니다.')