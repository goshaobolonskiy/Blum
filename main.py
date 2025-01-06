import requests
import time
import random
import sys
from config import headers, keywords

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')



def get_balance() -> object:
    response = requests.get("https://game-domain.blum.codes/api/v1/user/balance", headers=headers)
    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        print('Not Found.')
        return response
    else:
        print(response.status_code)
        return response

    


def end_farming() -> None:
    url : str = "https://game-domain.blum.codes/api/v1/farming/claim"
    for _ in range(1):
        response = requests.post(url, headers=headers)



def go_farming() -> None:
    for _ in range(1):
        response = requests.post("https://game-domain.blum.codes/api/v1/farming/start", headers=headers) # Запуск фарминга
        


def get_daily_reward() -> tuple:
    response = requests.get("https://game-domain.blum.codes/api/v2/daily-reward", headers=headers)

    if response.json()['claim'] == 'available':
        print(f'Reward available')
        return 1, response.json(), f"Current streak days {response.json()['currentStreakDays']}"
    else:
        return 0, response.json(), f"Current streak days {response.json()['currentStreakDays']}"
    


def post_daily_reward() -> dict:
    response = requests.post("https://game-domain.blum.codes/api/v2/daily-reward", headers=headers)

    return response.json()



session = requests.Session()
session.headers = headers

def get_sort_tasks() -> dict:
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


def process_tasks() -> None:
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


def start_task(task_id : str) -> int:
        url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/start"
        response = session.post(url)

        return response.status_code



def validate_task(task_id :str, keyword = str or None) -> None:
        url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/validate"
        if keyword is None:
            response = session.post(url, json={})
        else:
            response = session.post(url, json={"keywoard": keyword})

        if response.status_code != 200:
            return

        

def claim_task(task_id : str) -> None:        
        url = "https://earn-domain.blum.codes/api/v1/tasks/" + task_id + "/claim"
        response = session.post(url)
        if response.status_code != 200:
            return
        else:

            print(f'Task with id = {task_id} finished')



def start_game() -> None:

        playPasses = get_balance().json()["playPasses"]
        
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
        



def main() -> None:
    for _ in range(3):
        try:
            status = get_balance().status_code
            if status == 200:
                balance = get_balance().json()

                print(f'Balance = {balance["availableBalance"]}')
                print(f'Play passes = {balance["playPasses"]}')

                if "farming" in balance:                                     
                    if balance["farming"]["endTime"] <= balance["timestamp"]:
                        farm = "Go end_farming"
                                   
                        try:
                            end_farming()                                   
                        except ValueError as e:
                            print(f"Error: {e}")

                    else:
                        farm = "farming now"
                        print("farming now")

                else:
                    farm = "is not farming"
                    go_farming()





                if get_daily_reward()[0] == 1:
                    post_daily_reward()
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



def choose_number() -> None:
    while True:  
        try:  
            number = int(input(                
                """
                Введите число от 1 до 4:\n
                    1. Запуск main (Вывод баланса, сбор возможных наград, запуск фарминга)
                    2. Запуск выполнения задач
                    3. Игра в игру  (BlumPayloadGenerator)
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
                False
                break
            break
            
        except ValueError:  
            print("Ошибка: Пожалуйста, введите целое число.")  

choose_number()