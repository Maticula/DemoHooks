import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("url-https://discord.com/api/webhooks/960243712976367716/O20YxGzMUo7HOmebGMjwzvmBhUA_3kAoE-KRWoY5QLiYlL7lmQ4Ghse5TFp1hlHjLbNI", adapter=RequestsWebhookAdapter())
webhook.send("Commit")
