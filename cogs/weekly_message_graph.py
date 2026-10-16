import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect("message_log_new_est.db")
user_id = input("Enter a user ID: ")
query = "SELECT * FROM message_data WHERE user_id = ?"
df = pd.read_sql_query(query, conn, params=(user_id,))
conn.close()

if df.empty:
    print(f"No messages found for user ID: {user_id}")
else:
    df["date_sent"] = pd.to_datetime(df["date_sent"])
    df["week_start"] = (
        df["date_sent"].dt.to_period("W-MON").dt.start_time
    )
    weekly_counts = df["week_start"].value_counts().sort_index()
    weekly_pct_change = weekly_counts.pct_change() * 100
    weekly_counts.index = weekly_counts.index.strftime("%Y-%m-%d")

    plt.figure(figsize=(12, 6))
    bars = plt.bar(
        weekly_counts.index,
        weekly_counts.values,
        color="skyblue",
        edgecolor="black",
    )

    for i, bar in enumerate(bars):
        height = bar.get_height()
        if i > 0 and not pd.isna(weekly_pct_change.iloc[i]):
            pct = weekly_pct_change.iloc[i]
            text = f"{pct:+.1f}%"
            text_color = "green" if pct >= 0 else "red"
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height + (max(weekly_counts) * 0.01),
                text,
                ha="center",
                va="bottom",
                fontsize=9,
                color=text_color,
                weight="bold",
            )

    plt.title("Messages Sent by Week (with % Change)", fontsize=14)
    plt.xlabel("Week Start Date", fontsize=12)
    plt.ylabel("Number of Messages", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.ylim(0, max(weekly_counts) * 1.1)
    plt.tight_layout()
    plt.savefig("messages_per_week.png")
    plt.show()
