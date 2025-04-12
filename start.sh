#!/bin/bash
# 使用 Gunicorn 启动 Flask 应用
gunicorn -w 4 -b 0.0.0.0:5000 bot.webhook:app