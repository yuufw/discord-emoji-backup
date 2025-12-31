import os
import discord
from discord.ext import commands

import config
import utils

EMOJIS_PATH = "emojis"


class EmojiDownloader(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="$", intents=intents)
        self.emoji_utils = utils

    async def setup_hook(self):
        print("Bot inicializado.")

    def create_dirs_if_not_exists(self, guild_id: int):
        base_path = f"{EMOJIS_PATH}/{guild_id}"
        os.makedirs(f"{base_path}/animated", exist_ok=True)
        os.makedirs(f"{base_path}/static", exist_ok=True)

    def download_emojis(self, emojis: list, guild_id: int) -> int:
        downloaded_emojis = 0
        base_path = f"{EMOJIS_PATH}/{guild_id}"

        for emoji in emojis:
            safe_name = emoji.name.replace("/", "_")
            ext = "gif" if emoji.animated else "png"
            folder = "animated" if emoji.animated else "static"
            file_path = f"{base_path}/{folder}/{safe_name}.{ext}"

            if os.path.exists(file_path):
                print(f"Emoji {safe_name} já existe.")
                continue

            url = f"https://cdn.discordapp.com/emojis/{emoji.id}.{ext}"
            self.emoji_utils.download_emoji(url, file_path)
            downloaded_emojis += 1

        return downloaded_emojis

    async def on_ready(self):
        print(f"Logado como {self.user}")
        print(f"Conectado a {len(self.guilds)} guild(s).")

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Este servidor tem {len(ctx.guild.emojis)} emojis.")

    @commands.command(name="d")
    async def download(self, ctx):
        await ctx.send("📥 Baixando emojis...")

        guild = ctx.guild
        self.create_dirs_if_not_exists(guild.id)

        total_emojis = len(guild.emojis)
        downloaded = self.download_emojis(guild.emojis, guild.id)

        await ctx.send(
            f"✅ **Concluído!**\n"
            f"Total: {total_emojis}\n"
            f"Baixados: {downloaded}\n"
            f"Já existentes: {total_emojis - downloaded}"
        )

    def run_bot(self):
        os.system("cls" if os.name == "nt" else "clear")

        print(
            f"""{utils.colors.PINK}
             ______     _ _   _           _         
             |  ___|   (_|_) | |         | |        
             | |_ _   _ _ _  | |     __ _| |__  ___ 
             |  _| | | | | | | |    / _` | '_ \/ __|
             | | | |_| | | | | |___| (_| | |_) \__ \\
             \_|  \__,_| |_| \_____/\__,_|_.__/|___/
            {utils.colors.ENDC}"""
        )

        print(f"{utils.colors.RED}Created by: Fuji Labs{utils.colors.ENDC}")
        self.run(config.BOT_TOKEN)


if __name__ == "__main__":
    bot = EmojiDownloader()
    bot.run_bot()
