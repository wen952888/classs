package main

import (
	"log"
	"os"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

func main() {
	// 从环境变量中获取 Telegram bot token
	botToken := os.Getenv("TELEGRAM_BOT_TOKEN")
	if botToken == "" {
		log.Fatal("TELEGRAM_BOT_TOKEN is not set")
	}

	// 初始化 Telegram Bot API
	bot, err := tgbotapi.NewBotAPI(botToken)
	if err != nil {
		log.Fatalf("Failed to create bot: %v", err)
	}

	// 设置为 debug 模式
	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

	// 设置更新配置
	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates := bot.GetUpdatesChan(u)

	// 处理消息
	for update := range updates {
		if update.Message == nil { // 忽略非消息更新
			continue
		}

		log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

		// 回复消息
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Hello, "+update.Message.Text)
		bot.Send(msg)
	}
}