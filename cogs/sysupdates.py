import json
from datetime import datetime

import feedparser
from discord.ext import commands


class friiRSS(commands.Cog):
    async def check_sysupdates(self, ponged, roleid, bot):

        with open("info.json") as j:
            js = json.load(j)
            entries = js["sysupdates"]

        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Checking for sysupdates")

        feed = feedparser.parse("https://yls8.mtheall.com/ninupdates/feed.php")
        for entry in feed.entries:
            version = entry.title[7:]
            if version not in entries:
                if not ponged:
                    await self.send(f"<@&{roleid}> New firmware version detected!")
                await self.send(f"Version {version} released on: {entry.published}")
                entries.append(version)

        with open("info.json") as j:
            js = json.load(j)
            js["sysupdates"] = entries
            json.dump(js, j)

def setup(bot):
    bot.add_cog(friiRSS(bot))