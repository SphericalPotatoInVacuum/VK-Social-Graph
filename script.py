import requests as r
import config as cfg
from collections import deque
import sys
import time
import os

tree = dict()  #
d = dict()  #
q = deque()  #
used = dict()  #
pred = dict()  #
fout = open("order.txt", "w")


def nameFromID(id):
    response = r.get(
        "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, id))
    name = response.json()["response"][0]["first_name"]
    surname = response.json()["response"][0]["last_name"]
    return name + " " + surname


maxD, ids, idf = sys.argv[1:]
maxD = int(maxD)

start = time.clock()

response = r.get(
    "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, ids))
ids = response.json()["response"][0]["id"]
response = r.get(
    "https://api.vk.com/method/users.get?access_token={0}&user_ids={1}&v=5.75".format(cfg.token, idf))
idf = response.json()["response"][0]["id"]

q.append(ids)
d[ids] = 0
pred[ids] = ids
used[ids] = True
curD = 0
found = False
count = 0

while len(q) > 0 and curD <= maxD and not found:
    start = time.clock()
    v = q.popleft()
    curD = d[v]
    if v == idf:
        found = True
    response = None
    while response is None:
        try:
            response = r.get(
                "https://api.vk.com/method/friends.get?access_token={0}&user_id={1}&v=5.75".format(cfg.token, v), timeout=5)
        except r.exceptions.BaseHTTPError as e:
            print("Connection error, trying again in 2s")
            print()
            time.sleep(2)
            continue
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
        count += 1

    sys.stdout.write("\rTotal people checked: " + str(count))
    sys.stdout.flush()
    time.sleep(0.1)

print()
if found:
    if not os.path.exists("img"):
        os.makedirs("img")
    id = idf
    order = []
    while d[id] > 0:
        order.append(nameFromID(id))
        order.append(str(id))
        response = r.get(
            "https://api.vk.com/method/users.get?access_token={0}&fields=photo_max&user_ids={1}&v=5.75".format(cfg.token, id))
        imgR = r.get(response.json()["response"][0]["photo_max"])
        with open("img/" + str(id) + ".jpg", "wb") as img:
            img.write(imgR.content)
            img.close()
        id = pred[id]
    response = r.get(
        "https://api.vk.com/method/users.get?access_token={0}&fields=photo_max&user_ids={1}&v=5.75".format(cfg.token, id))
    imgR = r.get(response.json()["response"][0]["photo_max"])
    with open("img/" + str(id) + ".jpg", "wb") as img:
        img.write(imgR.content)
        img.close()
    order.append(nameFromID(id))
    order.append(str(id))
    order.reverse()
    print(len(order) // 2, file=fout)
    for id in order:
        print(id, file=fout)
    fout.close()
else:
    print("Sorry, finish id is out of max range")
