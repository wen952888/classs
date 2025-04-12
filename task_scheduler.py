from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

scheduler = AsyncIOScheduler()

def schedule_task(task_details):
    scheduler.add_job(func=execute_task, args=[task_details], trigger="interval", seconds=30)
    scheduler.start()
    logging.info(f"任务已添加: {task_details}")

async def execute_task(task_details):
    logging.info(f"执行任务: {task_details}")