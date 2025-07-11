import requests
from flask import request

@app.route('/api/webhooks/<webhook_id>/<webhook_token>', methods=['POST'])
def relay_discord_webhook(webhook_id, webhook_token):
    discord_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    try:
        response = requests.post(discord_url, json=request.get_json())
        return {"status": "ok", "discord_status": response.status_code}
    except Exception as e:
        return {"error": str(e)}, 500
