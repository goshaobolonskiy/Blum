import requests
import json
import time
import random
import pprint
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')





# Токен для аутентификации
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoYXNfZ3Vlc3QiOmZhbHNlLCJ0eXBlIjoiQUNDRVNTIiwiaXNzIjoiYmx1bSIsInN1YiI6ImEyZWQ2MjBmLWZhZmQtNGMzZi05YWIyLTVkZTVkOWJjZGRlYyIsImV4cCI6MTczNjA2OTIzNCwiaWF0IjoxNzM2MDY1NjM0fQ.UxGvuYnI3ThG6i0FuXn_pCKnLgn4KSl8yzWSWhhIO0w"







headers = {
    "Accept": 'application/json',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Authorization": f"Bearer {token}",
}

keywords = {
        "6af85c01-f68d-4311-b78a-9cf33ba5b151": "GO GET",
        "38f6dd88-57bd-4b42-8712-286a06dac0a0": "VALUE",
        "d95d3299-e035-4bf6-a7ca-0f71578e9197": "BEST PROJECT EVER",
        "53044aaf-a51f-4dfc-851a-ae2699a5f729": "HEYBLUM",
        "835d4d8a-f9af-4ff5-835e-a15d48e465e6": "CRYPTOBLUM",
        "3c048e58-6bb5-4cba-96cb-e564c046de58": "SUPERBLUM",
        "350501e9-4fe4-4612-b899-b2daa11071fb": "CRYPTOSMART",
        "b611352b-0d8c-44ec-8e0f-cd71b5922ca5": "BLUMERSSS",
        "92373c2b-2bf3-44c0-90f7-a7fd146c05c5": "HAPPYDOGS",
        "d2715289-b487-43bc-bc21-18224f8f6bc3": "NODOXXING",
        "7067a3db-d9c5-4268-ac19-c393743e8491": "WOWBLUM",
        "c60919cd-0282-46fe-854a-1da0a01db9b2": "Blum - Big City Life",
        "1572a605-d714-4f2c-8045-9c5f874d9c7e": "MEMEBLUM",
        "30d9f351-614e-4565-a1bb-e7e94fc3dc3c": "ONFIRE",
        "d2a972a1-12ab-4c7b-a411-da056609f2bd": "SOBLUM",
        "56d210c1-446b-473b-b7c4-cba856b4476c": "BLUMEXPLORER",
        "25928ae7-c3c2-40ba-bb78-975ed68e4a5a": "CRYPTOFAN",
        "dc627a62-f747-4cbb-981f-62cf82a85458": "BLUMTASTIC",
        "71ad89ea-f11f-4825-af9c-408fba7dfd8e": "BLUMFORCE",
        "a669a160-45fd-4935-9eda-58079e19aad5": "ULTRABLUM",
        "7491c933-e49d-4a60-89cd-53d9fe690dca": "BLUMSTORM",
        "900bc6e5-d73e-49fe-adf5-1f8111f1b431": "BLUMEXTRA",
        "6fb7499f-8b38-4132-8255-c3184cc2712c": "PUMPIT",
        "98d390d1-95da-475f-8df9-53a335842c3a": "BLUMHELPS",
        "92bc4338-85ca-4bf9-a0a5-320e677116fd": "FOMOOO",
        "bb84e765-31aa-4f0d-8430-b3f75d88c1aa": "CRYPTOZONE",
        "7a3502e2-cdc7-4842-8879-bbeb2ebec594": "BLUMIFY",
        "4477c434-f8df-4432-a3d7-b47a6e44c1d7": "DEXXX",
    }




def get_balance():
    response = requests.get("https://game-domain.blum.codes/api/v1/user/balance", headers=headers)
    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        print('Not Found.')
        return response
    else:
        print(response.status_code)
        return response



def end_farming():
    url = "https://game-domain.blum.codes/api/v1/farming/claim"
    for _ in range(1):
        response = requests.post(url, headers=headers)
        # print(response)
        # if response.status_code == 200:
        #     try:
        #         print(response.text)
        #         data = response.json()
        #         return data["gameId"]
            
        #     except ValueError as e:
        #         print(f"Ответ не в формате JSON: {e}")

def go_farming():
    for _ in range(1):
        response = requests.post("https://game-domain.blum.codes/api/v1/farming/start", headers=headers) # Запуск фарминга
        print(response)
        if response.status_code == 200:
            try:
                # print(response.text)
                print(response.json())

            
            except ValueError as e:
                print(f"Error: {e}")



def get_daily_reward(): # Проверить ежедневную награду
    response = requests.get("https://game-domain.blum.codes/api/v2/daily-reward", headers=headers)
    # pprint.pprint(response.json())
    if response.json()['claim'] == 'available':
        print(f'Reward available')
        return 1, response.json(), f"Current streak days {response.json()['currentStreakDays']}"
    else:
        return 0, response.json(), f"Current streak days {response.json()['currentStreakDays']}"
    



def post_daily_reward(): # Собрать ежедневную награду
    response = requests.post("https://game-domain.blum.codes/api/v2/daily-reward", headers=headers)
    # pprint.pprint(response.json())
    return response.json()



session = requests.Session()
session.headers = {
        "Accept": 'application/json',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Authorization": f"Bearer {token}",
    }


def get_sort_tasks():
        response = session.get("https://earn-domain.blum.codes/api/v1/tasks/")
        if not response.ok:
            raise Exception(
                "Can not get tasks "
                f"with status code {response.status_code}: {response.text}"
            )

        tasks: list | None = response.json()
        

        all_tasks = []
        collected_tasks = []

        for section in tasks:
            collected_tasks.extend(section.get("tasks", []))
            for sub_section in section.get("subSections"):
                collected_tasks.extend(sub_section.get("tasks", []))

        for task in collected_tasks:
            if task.get("subTasks"):
                all_tasks.extend(task.get("subTasks"))

        all_tasks.extend(collected_tasks)


        unique_tasks = {}
        task_types = ("SOCIAL_SUBSCRIPTION", "INTERNAL", "SOCIAL_MEDIA_CHECK")

        for task in all_tasks:
            if task.get("validationType") == "MEMEPAD":
                continue
            elif task.get("type") == "PROGRESS_TARGET":
                continue
            elif task.get("title") == "Join or create tribe":
                continue

            if (
                task["status"] == "NOT_STARTED"
                and task["type"] in task_types
                or task["status"] == "READY_FOR_CLAIM"
                or task["status"] == "READY_FOR_VERIFY"
                and task["validationType"] == "KEYWORD"
            ):
                unique_tasks.update({task.get("id"): task})

        return unique_tasks


def process_tasks():
    sorted_tasks = get_sort_tasks()

    for task_id in sorted_tasks:
        if start_task(task_id) == 200:
            time.sleep(2)
            if sorted_tasks.get(task_id).get("validationType") == "KEYWORD":  # type: ignore
                keyword = keywords.get(task_id)
                validate_task(task_id, keyword=keyword)
            else:
                validate_task(task_id)
            claim_task(task_id)
            time.sleep(2)

    print("Все возможные задачи выполнены")
    choose_number()


def start_task(task_id):
        url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/start"
        response = session.post(url)

        return response.status_code
        # if response.status_code != 200:
        #     return 
        

def validate_task(task_id, keyword = None):
        url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/validate"
        if keyword is None:
            response = session.post(url, json={})
        else:
            response = session.post(url, json={"keywoard": keyword})
        # print(response.status_code, 2)
        if response.status_code != 200:
            return

        


def claim_task(task_id):        
            url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/claim"
            response = session.post(url)
            if response.status_code != 200:
                return
            else:

                print(f'Task with id = {task_id} finished')
            # print(response.status_code, 3)
        



def start_game():

        playPasses = get_balance().json()["playPasses"]
        # playPasses = 1
        
        if playPasses <= 0:
            print("Not enough tikets to start play game")

            choose_number()
            return

        while playPasses >= 0:
            response = session.post("https://game-domain.blum.codes/api/v2/game/play")
            if response.ok:
                            
                sleep_time = random.uniform(30, 35)

                game_id = response.json().get("gameId")

                
                freezes = int((sleep_time - 30) / 3)

                blum_amount = random.randint(200, 230)
                earned_points = {"BP": {"amount": blum_amount}}
                asset_clicks = {
                    "BOMB": {"clicks": 0},
                    "CLOVER": {"clicks": blum_amount},
                    "FREEZE": {"clicks": freezes},
                }

                payload_data = {
                    "gameId": game_id,
                    "earnedPoints": earned_points,
                    "assetClicks": asset_clicks,
                }

                print("Игра запущена, ждем тайм-аут")
                time.sleep(sleep_time)

                payload_response = session.post(f"{"http://localhost:9876"}/getPayload", json=payload_data)
                payload = payload_response.json().get("payload")


                response = session.post("https://game-domain.blum.codes/api/v2/game/claim", json={"payload": payload})
                if response.status_code != 200:
                    print("Can not found game")
                    
                if not response.ok:
                    raise Exception(f"Can not claim game with status code {response.status_code}: {response.text}")
                
                
                if response.ok:
                    print(f"Claimed game, earned: {blum_amount}BP")

                if payload is None:
                    raise Exception("Can not parse pyload")
                playPasses -= 1
                
            else:
                raise Exception(f"Can not start play with status code {response.status_code}: {response.text}")
            
        choose_number()
        



def main():
    for _ in range(3):
        try:
            status = get_balance().status_code
            if status == 200:                                                   # Если запрос удачный, то продолжаем
                balance = get_balance().json()                                  # Получение json'а с баллансом

                print(f'Balance = {balance["availableBalance"]}')
                print(f'Play passes = {balance["playPasses"]}')                 # Количество билетов на игру

                if "farming" in balance:                                        # Если фарминг был запущен
                    if balance["farming"]["endTime"] <= balance["timestamp"]:   # Если фарминг закончился, то
                        farm = "Go end_farming"
                        # print("Go end_farming")                                         
                        try:
                            end_farming()                                       # собираем награду
                        except ValueError as e:
                            print(f"Error: {e}")

                    else:
                        farm = "farming now"
                        print("farming now")

                else:
                    farm = "is not farming"                                    # Если фарминг не был запущен, то
                    go_farming()                                                        # запускаем





                if get_daily_reward()[0] == 1:                           # Проверка получена ли дневная награда
                    post_daily_reward()                                  # Если не получена, то получаем
                    time.sleep(3)
                    print(f'Balance = {balance["availableBalance"]}')
                    print(get_daily_reward()[2])
                elif get_daily_reward()[0] == 0:
                    print(get_daily_reward()[2])

                choose_number()
                return balance["availableBalance"], balance["playPasses"], farm, get_daily_reward()[2]
            
            else:
                print(f'When trying to find out the balance, an error occurred {status} ; (token)')
                choose_number()
        except ValueError as e:
            print(f"Error: {e}")
    
    


# main()


def choose_number():  
    while True:  
        try:  
            number = int(input(                
                """
                Введите число от 1 до 4:\n
                    1. Запуск main (Вывод баланса, сбор возможных наград, запуск фарминга)
                    2. Запуск выполнения задач
                    3. Игра в игру
                    4. Выход
                    """))
            if number < 1 or number > 4:  
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 4.")  
                continue  
            
            if number == 1:
                main()
            elif number == 2:
                print("Начало выполнения задач..")
                process_tasks()

            elif number == 3:  
                print("Начало игры")
                start_game()
            elif number == 4:
                break
            break
            
        except ValueError:  
            print("Ошибка: Пожалуйста, введите целое число.")  

choose_number()
