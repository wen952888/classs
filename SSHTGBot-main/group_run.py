import asyncio
import logging
from ssh_utils import connect_to_ssh
from translations import get_translation

logging.basicConfig(level=logging.INFO)

DEFAULT_COMMAND = "uptime"

async def process_account(account, command):
    try:
        result = await connect_to_ssh(account, command)
        logging.info(f"{account['host']} 执行成功: {result}")
    except Exception as e:
        logging.error(f"{account['host']} 执行失败: {str(e)}")

async def main(accounts, command=DEFAULT_COMMAND):
    tasks = [process_account(account, command) for account in accounts]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    accounts = [{"host": "example.com", "username": "user", "password": "pass"}]
    asyncio.run(main(accounts))