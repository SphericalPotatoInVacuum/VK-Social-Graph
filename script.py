import requests as r
import config as cfg
from collections import deque
import sys
import time

tree = dict()  # Словарь с парами [id : список друзей]
d = dict()  # Словарь с парами [id : дистанция]
q = deque()  # Очередь для BFS
used = dict()  # Словарь посещений
pred = dict()  # Словарь предков

# Максимальная дистанция, после достижения которой поиск остановится
maxD = int(input())
ids = input()  # id, с которого начнётся поиск
idf = input()  # id, на котором он закончится

response = r.get(
    "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, ids))
ids = response.json()["response"][0]["id"]
response = r.get(
    "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, idf))
idf = response.json()["response"][0]["id"]

q.append(ids)
d[ids] = 0
pred[ids] = 0
used[ids] = True
curD = 0
found = False

while len(q) > 0 and curD <= maxD and not found:
    v = q.popleft()
    response = r.get(
        "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, v))
    curD = d[v]
    if v == idf:
        found = True
    response = r.get(
        "https://api.vk.com/method/friends.get?access_token={0}&user_id={1}&v=5.75".format(cfg.token, v))
    items = response.json().get("response", {"items": []})["items"]
    for item in items:
        if used.get(item, False):
            continue
        used[item] = True
        d[item] = d[v] + 1
        pred[item] = v
        if item == idf:
            found = True
            break
        q.append(item)
    time.sleep(0.5)

if found:
    id = idf
    while d[id] > 0:
        print(id)
        id = pred[id]
    print(id)

else:
    print("Sorry, finish id is out of max range")
