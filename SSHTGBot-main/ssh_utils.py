import asyncssh
import logging

async def connect_to_ssh(account, command):
    try:
        async with asyncssh.connect(account["host"], username=account["username"], password=account["password"]) as conn:
            result = await conn.run(command)
            return result.stdout
    except Exception as ex:
        logging.error(f"SSH 连接失败: {str(ex)}")
        raise