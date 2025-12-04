import zmq
import time
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:2222")

print("Сервер запущен на порту 2222")

counter = 0

def print_stats():
    print("\nСТАТИСТИКА СЕРВЕРА")
    print(f"Получено пакетов: {counter}")

    if os.path.exists("location.json"):
        with open("location.json", "r", encoding="utf-8") as file:
            try:
                all_data = json.load(file)
            except json.JSONDecodeError:
                all_data = []
    else:
        all_data = []

    print("Все JSON записи:")
    for idx, entry in enumerate(all_data, start=1):
        print(f"{idx}: {entry}")


while True:
    message = socket.recv()
    json_str = message.decode("utf-8")

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        socket.send(b"Error: invalid JSON")
        continue

    if os.path.exists("location.json"):
        with open("location.json", "r", encoding="utf-8") as file:
            try:
                current = json.load(file)
            except json.JSONDecodeError:
                current = []
    else:
        current = []

    current.append(data)

    with open("location.json", "w", encoding="utf-8") as file:
        json.dump(current, file, indent=4, ensure_ascii=False)

    counter += 1

    print_stats()

    reply = f"Пакет принят. Всего обработано: {counter}"
    socket.send(reply.encode("utf-8"))

    time.sleep(0.2)

