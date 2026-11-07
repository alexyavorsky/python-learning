import requests

API_TOKEN = "c5c8fd2b-7826-4bc9-af88-f226276dcad6"

URL = "https://api.weeek.net/public/v1/tm/tasks"

headers = {"Authorization": f"Bearer {API_TOKEN}",
           "Content-Type": "application/json"}

projects = requests.get(url="https://api.weeek.net/public/v1/tm/projects", headers=headers)
projects = projects.json()["projects"]
print("ID, Название проекта")
for idx, project in enumerate(projects, 1):
    print(idx, project["title"])

project_id = int(input("Выберете ID проекта: "))

boards_payload = {
    "projectId": project_id
}
boards = requests.get(url="https://api.weeek.net/public/v1/tm/boards", json=boards_payload, headers=headers)
boards = boards.json()["boards"]
print("ID, Название колонки")
for idx, board in enumerate(boards, 1):
    print(idx, board["name"])

board_id = int(input("Выберете ID таблицы: "))
columns_payload = {
    "boardId": board_id
}
columns = requests.get(url="https://api.weeek.net/public/v1/tm/board-columns", json=columns_payload, headers=headers)
columns = columns.json()["boardColumns"]
print("ID, название")
for idx, column in enumerate(columns, 1):
    print(idx, column["name"])

column_id = int(input("Введи ID колонки: "))

title = input("Введи название: ")
description = input("Введи текст карточки: ")

payload = {
    "locations": [{
        "projectId": project_id,
        "boardColumnId": column_id
    }],
    "title": title,
    "description": description,
    "day": "03.11.2026"
}

response = requests.post(url=URL, json=payload, headers=headers)

if response.json()["success"]:
    print("задача успешно создана")
