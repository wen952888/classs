<h1 align="center">SSH Master</h1>
<h3 align="center"><span style="font-size: 0.9em;"><a href="/README.md">简体中文</a></span> / <span style="font-size: 0.9em;">English</span></h3>

<div align="center">
    <strong>🚀 Lightweight SSH/SFTP Remote Management Tool | <a href="https://ssh.argofusion.com">Online Version</a></strong>
</div>

<div align="center">
    <p>📢 Open Source Version Update Coming: Support for SFTP and Better User Experience</p>
    <p>🌟 Online Version Available: <a href="https://ssh.argofusion.com">https://ssh.argofusion.com</a></p>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Status-Coming Soon-orange" alt="Status">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
</p>

## ✨ Key Features

- 🔐 **Authentication**: Support for password and key authentication
- 🌐 **Web Terminal**: Manage SSH connections in browser(WEBSSH)
- 📂 **SFTP Features**: File upload, download and editing capabilities
- 📱 **Mobile Support**: Compatible with mobile devices
- 🔄 **Batch Operations**: Execute commands on multiple servers
- ⏰ **Scheduled Tasks**: Basic task management
- 👥 **Group Management**: Server grouping functionality
- 🌍 **Bilingual**: Chinese and English interface

## 🎯 Use Cases

- Server maintenance
- Batch command execution
- File transfer management
- Scheduled task execution
- Mobile management

## 🚀 Online Version

Visit the online version: [https://ssh.argofusion.com](https://ssh.argofusion.com)

## 📝 Version Information

This is the open-source version of SSH Master, providing basic SSH connection and management features, with SFTP support coming soon. The online version additionally offers:

- Multi-user permission management system

Online version: [https://ssh.argofusion.com](https://ssh.argofusion.com)

## 🤝 Contributing

Issues and Pull Requests are welcome to help improve this project.

## 📜 License

This project is licensed under the MIT License. Please comply with the open source license when using it.

## Project Overview

SSH Master is a Telegram-based automation tool primarily designed for remote management and scheduled or manual execution of commands on multiple hosts (such as serv00). This project allows users to p[...]

### Key Features

1. Remote control of hosts via Telegram bot interface
2. Support for SSH connections to multiple hosts
3. Execution of custom commands or predefined scripts
4. Scheduling of script execution tasks
5. Support for key-based authentication
6. Support for bulk public key upload
7. Support for scheduled task management (New)
8. Support for host grouping (New)
9. Support for time mode switching (hours/minutes) (New)

## Telegram Discussion Group

We welcome you to join our Telegram discussion group. Here you can discuss usage experiences with other users, get help, and stay updated on the latest project developments:

[Join SSH Master Discussion Group](https://t.me/+WIX6H-944HQzZmQ9)

## Deployment Method

### Prerequisites

1. A Telegram bot Token. Search for BotFather in Telegram, create a new Bot, and obtain the API Token.
2. Your Telegram user ID. To get this: Send a message to the Bot, then visit `https://api.telegram.org/bot<Your_API Token>/getUpdates` to obtain the Chat ID.
3. A Render account (for deployment)
4. Your host account information (including SSH username, password, and SSH address)

### Deployment Steps

1. Fork this project to your GitHub account.

2. Create a new Web Service in Render and connect it to your forked GitHub repository.

3. Set the following environment variables in Render:
   - `LAUNUAGE`:zh/en, Default language is Chinese
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot Token
   - `TELEGRAM_CHAT_ID`: Your Telegram user ID 
   - `ACCOUNTS_JSON`: JSON string containing host account information, formatted as follows:
     ```json
     [
       {
         "customhostname": "customhostname1", (Custom host name, recommended to set)
         "ssluser": "your_ssluser1", (SSH username)
         "password": "your_password1", (SSH password)
         "sslhost": "your_sslhost1", (SSH address, format example: "s5.serv00.com")
         "secretkey": "private key path 1 including private key file", (Optional, used to upload private key to render, set in Secret Files under render environment variables. Format example: /etc/sec[...]
         "publickey": "public key path 1 including public key file, file extension .pub" (Optional, note no comma at the end of this line. Used to upload public key to SSH host, set in Secret Files un[...]
       },
       {
         "customhostname": "customhostname2",
         "ssluser": "your_ssluser2",
         "password": "your_password2",
         "sslhost": "your_sslhost2",
         "secretkey": "private key path 2",
         "publickey": "public key path 2"
       },     
       ...
     ]
     ```
   - `AUTO_CONNECT_INTERVAL`: Cycle time for scheduled tasks, optional, integer default 24, can be disabled by entering /set_cron 0 in telegram after deployment.
   - `RENDER_APP_URL`: Your Render application URL (format: https://*******.onrender.com, top left of the project, no / at the end of the address)
   - `CUSTOM_COMMAND`: Initial custom execution command (when set, custom commands will not be cleared after Render redeploys)
   - `TIME_MODE`: Time unit mode (hour/minute) sets whether the cycle unit is hours or minutes, minute mode allows for more precise control, default is hour mode.
   - `CRON_TASKS_JSON`: Scheduled tasks and host group configuration (New), formatted as follows:
     ```json
     {
         "tasks": [
             {
                 "id": "1", (Task number)
                 "command": "uptime", (Custom command)
                 "interval": 1, (Cycle time, hours in hour mode, minutes in minute mode)
                 "variation": 10, (Deviation time, minutes in hour mode, seconds in minute mode)
                 "target": "all"
             },
             {
                 "id": "2",
                 "command": "df -h",
                 "interval": 1,
                 "variation": 5,
                 "target": "+3" (First three hosts in ACCOUNTS_JSON, -3 would indicate the last 3 hosts)
             },
             {
                 "id": "3",
                 "command": "custom_command",
                 "interval": 1,
                 "variation": 2,
                 "target": "flypig,maxjiu,group:group2" (Host groups need to be prefixed with group:)
             }
         ],
         "host_groups": {
             "group1": [
                 "flypig",
                 "maxjiu"
             ],
             "group2": [
                 "hycl",
                 "happyboy"
             ]
         }
     }
     ```

4. Start Docker in Render.

Note: Render allows deployment of one free project, which may experience a 50s delay if not accessed for a long time. You can download UptimeRobot on your phone to keep it active for free.