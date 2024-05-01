import asyncio
from typing import Annotated

import typer

from . import new_bot_client

app = typer.Typer()


@app.command()
def run(token: Annotated[str, typer.Argument(envvar="DISCORD_TOKEN")]):
    bot = new_bot_client()
    asyncio.run(bot.run(token))

if __name__ == "__main__":
    app()