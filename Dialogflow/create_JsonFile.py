from import_data import *   #import_data.py 의 모든 개체와 메서드를 가져온다.
import json

# 파일로 출력하기
i = 0

prev_content = str(conversations[0].contentName) + str(conversations[0].contentType)

# 사용자가 데이터를 저장할 목록 생성
user_says_data = []

while i < len(conversations):
    c = conversations[i]
    current_content = str(c.contentName) + str(c.contentType)
    # 새로운 current_content 가 나올때마다 초기화하고 다른 파일을 생성하여 저장.
    # contentName과 contentType이 다를 경우에만 새로운 파일을 생성하여 중복 생성을 방지한다.
    if current_content != prev_content:
        # 데이터를 파일에 쓰기
        with open(f'{prev_content}_usersays_ko.json', 'w', encoding='UTF-8') as f:
            json.dump(user_says_data, f)
        # 다음 새 목록을 생성하여 데이터를 정의합니다.
        user_says_data = []
        prev_content = current_content
    # 현재 대화의 질문을 사용자가 데이터 목록에 추가합니다. 양식은 BigdataUpload_usersays_ko.json을 맞춥니다.
    user_says_data.append({
        "id": "1c940faa-ff3c-4278-b096-83efb4210d0f",
        "data": [
            {
            "text": c.question,
            "userDefined": False
            }
        ],
        "isTemplate": False,
        "count": 0,
        "lang": "ko",
        "updated": 0
        })

    i += 1

    # 최종 사용자가 말하는 데이터를 파일에 쓰기
    with open(f'{prev_content}_usersays_ko.json', 'w', encoding='UTF-8') as f:
        json.dump(user_says_data, f)

    # question 부분을 별도의 파일에 작성
    for c in conversations:
        current_content = str(c.contentName) + str(c.contentType)
        with open(f'{current_content}.json', 'w', encoding='UTF-8') as f:
            json.dump({
                "id": "0f2895c5-84b1-4827-9955-45893ea22920",
                "name": current_content,
                "auto": True,
                "contexts": [],
                "responses": [{
                    "resetContexts": False,
                    "affectedContexts": [],
                    "parameters": [
                        {
                            "id": "47fcb256-c212-43fb-b75d-0d287919c303",
                            "name": "language",
                            "required": False,
                            "dataType": "@sys.language",
                            "value": "$language",
                            "defaultValue": "",
                            "isList": False,
                            "prompts": [],
                            "promptMessages": [],
                            "noMatchPromptMessages": [],
                            "noInputPromptMessages": [],
                            "outputDialogContexts": []
                        }
                    ],
                    "messages": [
                        {
                        "type": 0,
                        "title": "",
                        "textToSpeech": "",
                        "lang": "ko",
                        "speech": c.answer,
                        "condition": ""
                    }],
                    "speech": []
                }],
                "priority": 500000,
                "webhookUsed": False,
                "webhookForSlotFilling": False,
                "fallbackIntent": False,
                "events": [],
                "conditionalResponses": [],
                "condition": "",
                "conditionalFollowupEvents": []
            }, f)

