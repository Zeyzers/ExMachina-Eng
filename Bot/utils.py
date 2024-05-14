from setup import *

async def __sync_commands_to_guild(self, guild: discord.Guild):
        """!
        Function to push all commands to a guild
        Doing this for all guilds on startup is is inefficient, but a fast way to push new commands to all guilds
        """
        try:
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        except discord.errors.Forbidden:
            print(f"Don't have the permissions to push slash commands to: '{guild.name}'")



# Function to generate help message dynamically
def generate_help_message(ctx):
    embed = discord.Embed(title='# Bot Commands', description='### Here are the available commands and their descriptions:', color=discord.Color.dark_purple())

    sorted_commands = sorted(client.commands, key=lambda cmd: cmd.name)
    for command in sorted_commands:
        if not command.hidden:
            embed.add_field(name=f"**[-{command.name}]**", value=command.description, inline=False)

    return embed

