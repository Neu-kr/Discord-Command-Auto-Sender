import requests
import json
import random
import time
import asyncio

# User token 
TOKEN = ""

# Command details
COMMANDS = [
    {
        "application_id": "",
        "guild_id": "",
        "channel_id": "",
        "command_id": "",
        "command_version": "",
        "command_name": "",
        "command_options": [],
        "interval": 0
    },
    {
        "application_id": "",
        "guild_id": "",
        "channel_id": "",
        "command_id": "",
        "command_version": "",
        "command_name": "",
        "command_options": [],
        "interval": 0
    }
]

# API endpoint & headers
API_URL = "https://discord.com/api/v9/interactions"
HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

def create_payload(command):
    return {
        "type": 2,
        "application_id": command["application_id"],
        "guild_id": command["guild_id"],
        "channel_id": command["channel_id"],
        "session_id": "4af5ac06ff895d243f2fc47e07ad5491",
        "data": {
            "version": command["command_version"],
            "id": command["command_id"],
            "name": command["command_name"],
            "type": 1,
            "options": command["command_options"],
            "application_command": {
                "id": command["command_id"],
                "type": 1,
                "application_id": command["application_id"],
                "version": command["command_version"],
                "name": command["command_name"],
                "options": [],
                "dm_permission": True,
                "integration_types": [0]
            },
            "attachments": []
        },
        "analytics_location": "slash_ui"
    }

async def send_command(command):
    while True:
        try:
            payload = create_payload(command)
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            if response.status_code == 204:
                print(f"\033[92m[✅ {timestamp}] [{command['command_name'].upper()}] Command sent successfully!\033[0m")
            elif response.status_code == 429:
                rate_limit_data = response.json()
                wait_time = rate_limit_data.get("retry_after", 1.0)
                print(f"\033[93m[⚠️ {timestamp}] [{command['command_name'].upper()}] Rate limited. Retrying after {wait_time:.2f} seconds...\033[0m")
                await asyncio.sleep(wait_time)
                continue
            else:
                print(f"\033[91m[❌ {timestamp}] [{command['command_name'].upper()}] Error: {response.status_code} - {response.text}\033[0m")

        except Exception as e:
            print(f"\033[91m[❌ ERROR] Exception occurred: {e}\033[0m")
            await asyncio.sleep(5)

        await asyncio.sleep(command["interval"])

async def main():
    tasks = [send_command(command) for command in COMMANDS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Script stopped.")
