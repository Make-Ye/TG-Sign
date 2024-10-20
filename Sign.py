import asyncio
import schedule
import time
from datetime import datetime, timedelta
from telethon import TelegramClient

api_id = []  # 输入api_id，一个账号一项
api_hash = ['']  # 输入api_hash，一个账号一项
bots = [
    ("https://t.me/xxx",'/sign', False),
    ("@xxxbot",'/sign', True),
]

async def sign_in(client, bot, command):
    try:
        await client.send_message(bot, command)
        await asyncio.sleep(5)  # 延时5秒，等待机器人回应
        await client.send_read_acknowledge(bot)
    except Exception as e:
        print(f"Failed to send message to {bot}: {e}")

async def main():
    for num in range(len(api_id)):
        session_name = f"id_{api_id[num]}"
        client = TelegramClient(session_name, api_id[num], api_hash[num])
        await client.start()
        tasks = [sign_in(client, bot, command) for bot, command, _ in bots]
        await asyncio.gather(*tasks)
        print(f"Done! Session name: {session_name}")
        await client.disconnect()

def schedule_task():
    asyncio.run(main())

def main_scheduler():
    schedule_task()
    # 初始运行时间设定为次日凌晨0点
    next_run_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    while True:
        now = datetime.now()
        if now >= next_run_time:
            schedule_task()
            next_run_time += timedelta(days=1, minutes=1)  # 每天增加1分钟
        time.sleep(60)  # 检查是否到达下次运行时间

if __name__ == "__main__":
    main_scheduler()
