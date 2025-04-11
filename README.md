# Telegram Subscription Bot with Flask

## Features
- Parse subscription links (Clash, SSR, V2Ray)
- Node health check
- Generate QR codes
- Support for multiple languages

## Setup and Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export TELEGRAM_TOKEN="your-telegram-bot-token"
export PORT=5000
```

### 3. Run the Application Locally
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

### 4. Deployment
You can deploy this application to any server or platform that supports WSGI servers like Gunicorn or uWSGI.