import asyncio
from typing import Callable, Iterable, List, Never, Type
import discord
from dataclasses import dataclass

from discord.app_commands.tree import CommandTree
from discord.ext import commands
from discord.ext.commands.bot import _default


listener = commands.Cog.listener
command = commands.command


@dataclass
class Greetings(commands.Cog):
    bot: commands.Bot
    last_member: discord.Member | None = None
    __hash__ = commands.Cog.__hash__

    @listener()
    async def on_member_join(self, member: discord.Member):
        if (channel := member.guild.system_channel) is not None:
            await channel.send(f"Hi {member.mention}!")

    @command("hello")
    async def hello(self, context, *, member: discord.Member | None = None) -> None:
        print("IN HELLO")
        member = member or context.member
        message = f"Hello {member.name}... this seems familiar"
        if self.last_member is None or self.last_member.id != member.id:
            message = f"Hello {member.name}~"

        await context.send(message)
        self.last_member = member


class Bot(commands.Bot):
    def __init__(self, *args, cog_library: List[commands.Cog], **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__cog_library = cog_library

    async def on_ready(self):
        print("== ready")

    async def setup_hook(self):
        await super().setup_hook()
        for cog in self.__cog_library:
            await self.add_cog(cog(self))


def new_bot_client() -> commands.Bot:
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    return Bot(command_prefix="^", intents=intents, cog_library=[Greetings])