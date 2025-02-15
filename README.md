# Discord Command Auto-Sender

## Overview
This script automates the sending of predefined Discord slash commands at scheduled intervals. It is useful for automating tasks like bumping servers or other periodic interactions with Discord bots.

## Features
- Supports multiple Discord slash commands.
- Handles rate limits automatically to prevent API bans.
- Asynchronous execution for efficient command scheduling.
- Customizable command list.
- Detailed logging to track command execution.
- Simple and lightweight implementation.

## Installation

### Prerequisites
- Python 3.7+
- `requests` and `asyncio` libraries

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/discord-command-auto-sender.git
   cd discord-command-auto-sender
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Set up your configuration:
   - Edit the `TOKEN` variable with your bot token.
   - Fill in the `COMMANDS` list with the required details.

## Usage
Run the script:
```bash
python auto_sender.py
```

## Configuration
Edit the `COMMANDS` list inside `auto_sender.py` to define the commands you want to automate. Example:
```python
COMMANDS = [
    {
        "application_id": "YOUR_APP_ID",
        "guild_id": "YOUR_GUILD_ID",
        "channel_id": "YOUR_CHANNEL_ID",
        "command_id": "YOUR_COMMAND_ID",
        "command_version": "YOUR_COMMAND_VERSION",
        "command_name": "bump",
        "command_options": [],
        "interval": 7200  # Interval in seconds
    }
]
```
### Command Execution Details
- The script continuously runs and executes each command at the specified interval.
- If a rate limit is encountered, it will wait for the required time before retrying.
- Error handling is included to catch any API failures.

## Handling Rate Limits
The script automatically detects rate limits and waits for the required duration before retrying. This helps avoid hitting Discord's API limits.

## License
MIT License

---

# Discord Command Auto-Sender (日本語版)

## 概要
このスクリプトは、Discordのスラッシュコマンドを定期的に自動送信するものです。disboardの定期bumpなどに利用することを目的としています。

## 特徴
- 複数のDiscordスラッシュコマンドをサポート。
- API制限（レートリミット）を自動処理。
- 各コマンドは非同期で実行。
- コマンドリストのカスタマイズが可能。
- 実行履歴のログをターミナルに出力。
- それなりにシンプル。

## インストール

### 必要なもの
- Python 3.7以上
- `requests` と `asyncio` ライブラリ

### セットアップ
1. このリポジトリをクローン:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/discord-command-auto-sender.git
   cd discord-command-auto-sender
   ```
2. 必要なライブラリをインストール:
   ```bash
   pip install requests
   ```
3. 設定を行う:
   - `TOKEN` 変数にボットのトークンを入力。
   - `COMMANDS` リストに必要な情報を記入。

## 使い方
スクリプトを実行:
```bash
python auto_sender.py
```

## 設定方法
`auto_sender.py` 内の `COMMANDS` リストを編集し、自動実行するコマンドを設定します。
```python
COMMANDS = [
    {
        "application_id": "YOUR_APP_ID",
        "guild_id": "YOUR_GUILD_ID",
        "channel_id": "YOUR_CHANNEL_ID",
        "command_id": "YOUR_COMMAND_ID",
        "command_version": "YOUR_COMMAND_VERSION",
        "command_name": "bump",
        "command_options": [],
        "interval": 7200  # 実行間隔（秒）
    }
]
```
### コマンドの実行詳細
- スクリプトは常に実行され、指定された間隔でコマンドを送信。
- レートリミットが発生した場合、指定時間待機後に再試行。
- APIエラー発生時は自動的に処理。

## レートリミット対策
スクリプトはAPIのレートリミットを自動検出し、指定時間待機してから再試行します。

## ライセンス
MITライセンス

