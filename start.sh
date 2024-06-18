#!/bin/bash
# This script sets the webhook URL for the Telegram bot

# Set your bot token
BOT_TOKEN="7217822006:AAG69nqMhQ-UTyHFLOJ1zqxADC9UPq_mOV8"

# Set the webhook URL (your Render URL)
WEBHOOK_URL="https://GitDownloder.onrender.com/$BOT_TOKEN"

# Set the webhook
curl -F "url=$WEBHOOK_URL" "https://api.telegram.org/bot$BOT_TOKEN/setWebhook"

# Start the Flask app
exec gunicorn --bind 0.0.0.0:$PORT app:app
