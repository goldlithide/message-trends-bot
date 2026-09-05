# Message Counter & Trends

Message Counter & Trends is a Python‑based analytics bot that transforms Discord activity into structured, long‑term behavioral insights. Refactored with SQLite, it stores timestamped message data in a persistent database, enabling scalable time‑series analysis and multi‑week comparisons. The bot can generate bar graphs, weekly trend visualizations, and percentage‑change statistics. It supports both personal and server‑wide analytics.

## Installation

1. Download or clone the repository.
2. Set up the bot on a local machine or a hosting service such as bot-hosting.net.
3. Open `main.py` and replace the placeholder value for `BOT_TOKEN` with your Discord bot token.
4. Install the required dependencies.
5. Start the bot.

## Usage

Run the following commands in a Discord server where the bot is installed.

### `/getMessageCounts [server_id]`

Collects message counts from the specified server and saves the data to a JSON file for later analysis.

### `/msgcounts`

Displays message counts grouped by channel, allowing users to identify the most active and least active channels in the server.

### `/getTrendGraph me|all`

Generates a weekly message activity trend graph for either:

- `me` — your personal message activity
- `all` — the entire server's message activity

## Hosting

The bot can be hosted locally or using hosting platforms such as bot-hosting.net.

## Data Collection

The bot logs message activity to a local SQLite database file. For each message, it records the timestamp, including the date and time.

## Features

- Store message data in a SQLite database
- Query multi‑week activity patterns using fast SQL lookups
- Generate clustered bar graphs comparing message volume across weeks
- Calculate weekly percentage changes to show increases or decreases in activity
- Identify peak activity periods


## Notes

- The bot requires the appropriate Discord permissions to read messages and generate statistics.
- Message data is stored locally on the host machine.
- Ensure that your usage complies with Discord's Terms of Service and your server's privacy policies when collecting and analyzing message data.
