from discord.ext import commands
import discord
from dataclasses import dataclass
from datetime import datetime
import aiofiles
import json
from dataclasses import asdict
from zoneinfo import ZoneInfo

@dataclass
class MessageData:
    date_sent: str
    time_sent: str
    day_of_week: int
    hour: int
    user_id: int
        
    @classmethod
    def get_message_data(cls, message):
        et_time = message.created_at.astimezone(ZoneInfo("America/New_York"))
        return cls(
            date_sent=et_time.strftime("%Y-%m-%d"),
            time_sent=et_time.strftime("%H:%M:%S"),
            day_of_week=et_time.weekday(),
            hour=et_time.hour,
            user_id = message.author.id
        )


class message_data_collection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    async def get_all_message_data(self, ctx, server_id: int):
        guild = self.bot.get_guild(server_id)
        if not guild:
            print(f"Guild with ID {server_id} not found.")
            return

        filename = "message_log_new_est.json"

        try:
            async with aiofiles.open(filename, "r") as f:
                content = await f.read()
                data = json.loads(content) if content else []
        except FileNotFoundError:
            data = []

        for channel in guild.text_channels:
            print("iterating through " + channel.name)
            try:
                async for message in channel.history(limit=None):
                    if message.type == discord.MessageType.default:
                        data_point = MessageData.get_message_data(message)
                        data.append(asdict(data_point))
            except discord.Forbidden:
                continue
            except discord.HTTPException as e:
                print(f"Failed to fetch history for {channel.name}: {e}")

        async with aiofiles.open(filename, "w") as f:
            await f.write(json.dumps(data, indent=4))            
    

async def setup(bot):
    await bot.add_cog(message_data_collection(bot))
