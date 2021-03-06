import os
from logging import Logger

from discord.ext.commands import Bot, Context, command

from cogs.utils.game import Game
from cogs.utils.werewolf_bot import WerewolfBot
from setup_logger import setup_logger


def main() -> None:
    logger: Logger = setup_logger(__name__)
    logger.info("START")

    # 接頭辞を「;」に設定
    bot: WerewolfBot = WerewolfBot(command_prefix=";")
    bot.game = Game()
    logger.debug(bot)

    # 環境変数DISCORD_BOT_TOKENからBOTのトークンを取得
    token = os.environ["DISCORD_BOT_TOKEN"]

    # コマンド「;ping」を追加
    # コマンドの内容は ping()を参照
    bot.add_command(ping)

    extension_list = [
        "cogs.players_cog",
        "cogs.game_status_cog",
    ]
    for extension in extension_list:
        bot.load_extension(name=extension)

    # bot実行
    bot.run(token)


@command()
async def ping(ctx: Context) -> None:
    """「;ping」と入力したら「pong」と返ってくる

    :param ctx:
    :return: None
    """
    await ctx.send("pong")


if __name__ == "__main__":
    main()
