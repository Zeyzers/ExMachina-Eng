from setup import *
import utils
client.remove_command('help')

@client.event
async def on_ready():
    member_count = 0
    guild_string = ''
    for g in client.guilds:
            guild_string += f"{g.name} - {g.id} - Members: {g.member_count}\n"
            member_count += g.member_count
            print(g)
            await utils.__sync_commands_to_guild(client, g)

    print(f"\n---\n"
        f"Bot '{client.user.name}' has connected, active on {len(client.guilds)} guilds:\n{guild_string}"
        f"---\n"
    )

        # set the status of the bot
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.custom, name='Use -help', state= 'Use -help')
    )


# Define a function to start typing
async def start_typing(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)

# Define a function to stop typing
async def stop_typing(ctx):
    await asyncio.sleep(1)  # Add a delay to ensure typing indicator is visible


# Register start_typing as a before_invoke for all commands
@client.before_invoke(start_typing)
async def before_command_invoke(ctx):
    pass

# Register stop_typing as an after_invoke for all commands
@client.after_invoke(stop_typing)
async def after_command_invoke(ctx):
    pass


@client.command(name='help', description='Displays available commands and their descriptions')
async def help_command(ctx):
    await ctx.send(embed=utils.generate_help_message(ctx))

@client.tree.command(name='help', description='Displays available commands and their descriptions')
async def help_command(ctx):
    await ctx.response.send_message(embed=utils.generate_help_message(ctx))


@client.tree.command(name='ping', description='It provides the latency between the server and the API')
async def ping(ctx):
    await ctx.response.send_message(f"🏓Latency is {round(client.latency * 1000)}ms.")

@client.command(name='ping', description='It provides the latency between the server and the API')
async def ping(ctx):
    await ctx.send(f"🏓Latency is {round(client.latency * 1000)}ms.")








@client.tree.command(name='userinfo', description='Display informations about a user')
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.user
    roles = [role.mention for role in user.roles]
    embed = discord.Embed(title=f'User Info: {user.display_name}#{user.discriminator}', color=discord.Color.green())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Created at', value=user.created_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Joined Server', value=user.joined_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Roles', value=', '.join(roles), inline=False)
    await ctx.response.send_message(embed=embed)


@client.command(name='userinfo', description='Display informations about a user')
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.author
    roles = [role.mention for role in user.roles]
    embed = discord.Embed(title=f'User Info: {user.display_name}#{user.discriminator}', color=discord.Color.green())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Created at', value=user.created_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Joined Server', value=user.joined_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Roles', value=', '.join(roles), inline=False)
    await ctx.send(embed=embed)



@client.tree.command(name='serverinfo', description='Display information about the server')
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(title=f'Server Info: {server.name}', color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon)
    embed.add_field(name='Owner', value=server.owner, inline=False)
    embed.add_field(name='Members', value=server.member_count, inline=False)
    embed.add_field(name='Creation Date', value=server.created_at.strftime('%Y-%m-%d'), inline=False)
    await ctx.response.send_message(embed=embed)


@client.command(name='serverinfo', description='Display information about the server')
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(title=f'Server Info: {server.name}', color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon)
    embed.add_field(name='Owner', value=server.owner, inline=False)
    embed.add_field(name='Members', value=server.member_count, inline=False)
    embed.add_field(name='Creation Date', value=server.created_at.strftime('%Y-%m-%d'), inline=False)
    await ctx.send(embed=embed)




@client.tree.command(name='roll', description='It rolls a custom quantity of dices with a custom number of sides')
async def roll(ctx, qty: int, sides: int):
    rolls = [random.randint(1, sides) for i in range(qty)]
    plural = 'dices' if len(rolls)>1 else 'die'
    await ctx.response.send_message(f'Rolling {qty} {plural} with {sides} sides: {rolls}')

@client.command(name='roll', description='It rolls a custom quantity of dices with a custom number of sides')
async def roll(ctx, qty: int, sides: int):
    rolls = [random.randint(1, sides) for i in range(qty)]
    plural = 'dices' if len(rolls)>1 else 'die'
    await ctx.send(f'Rolling {qty} {plural} with {sides} sides: {rolls}')



@client.command(name='kick', description='Kicks a user from the server with an optional reason')
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.author.guild_permissions.kick_members:
        if reason is None:
            reason = "No reason provided."
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked from the server. Reason: {reason}")
    else:
        await ctx.send("You don't have permission to use this command.")


@client.tree.command(name='kick', description='Kicks a user from the server with an optional reason')
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    author = ctx.user
    if author.guild_permissions.kick_members:
        if reason is None:
            reason = "No reason provided."
        await member.kick(reason=reason)
        await ctx.response.send_message(f"{member.mention} has been kicked from the server. Reason: {reason}")
    else:
        await ctx.response.send_message("You don't have permission to use this command.")



@client.command(name='ban', description='Bans a user from the server with an optional reason')
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.author.guild_permissions.ban_members:
        if reason is None:
            reason = "No reason provided."
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned from the server. Reason: {reason}")
    else:
        await ctx.send("You don't have permission to use this command.")


@client.tree.command(name='ban', description='Bans a user from the server with an optional reason')
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.user.guild_permissions.ban_members:
        if reason is None:
            reason = "No reason provided."
        await member.ban(reason=reason)
        await ctx.response.send_message(f"{member.mention} has been banned from the server. Reason: {reason}")
    else:
        await ctx.response.send_message("You don't have permission to use this command.")


@client.command(name='pardon', description='Unban a user that was previously banned from the server.')
async def pardon(ctx, user_id: int):
    if ctx.user.guild_permissions.ban_members:
        # Fetch the banned user
        banned_user = await ctx.guild.fetch_ban(discord.Object(id=user_id))

        # Unban the user
        await ctx.guild.unban(banned_user.user)

        # Inform the user about the unbanned user
        await ctx.send(f"{banned_user.user.name}#{banned_user.user.discriminator} has been unbanned from the server.")
    else:
        await ctx.send("You don't have permission to use this command.")



@client.command(name="clear", description="Clears a specified amount of messages from the current channel")
async def clear(ctx: commands.Context, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.send(f"Clearing {amount} messages.")
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("You don't have permission to use this command.")

@client.tree.command(name="clear", description="Clears a specified amount of messages from the current channel")
async def clear(ctx: commands.Context, amount: int):
    if ctx.user.guild_permissions.manage_messages:
        await ctx.response.send_message(f"Clearing {amount} messages.")
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.response.send_message("You don't have permission to use this command.")


@client.command(name='lockdown', description='Lock or unlock a channel to restrict or allow user messages.')
async def lockdown(ctx, channel: discord.TextChannel, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == 'lock':
            # Lock the channel
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f"{channel.mention} has been locked. Users can no longer send messages.")
        elif action.lower() == 'unlock':
            # Unlock the channel
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f"{channel.mention} has been unlocked. Users can now send messages.")
        else:
            await ctx.send("Invalid action. Please specify 'lock' or 'unlock'.")


@client.command(name='rolereact', description='Set up role reactions for users to self-assign roles by reacting to messages.')
async def rolereact(ctx):
    # Fetch existing roles of the server and convert to a list
    roles = list(ctx.guild.roles)

    # Remove @everyone role from the list
    roles.remove(ctx.guild.default_role)

    # Prompt the admin to select roles and emojis
    await ctx.send("Please select roles and their corresponding emojis to add as reactions to the message. Format: role_mention:emoji, role_name:emoji, ...")
    try:
        response = await client.wait_for('message', timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond.")
        return

    # Parse the admin's response and validate selected roles and emojis
    role_emoji_pairs = [pair.strip().split(':') for pair in response.content.split(',')]
    valid_pairs = []
    for pair in role_emoji_pairs:
        if len(pair) == 2:
            role, emoji = pair
            role = role.strip()
            emoji = emoji.strip()
            # Check if role is mentioned
            if role.startswith('<@&') and role.endswith('>'):
                role_id = int(role[3:-1])
                role_object = discord.utils.get(ctx.guild.roles, id=role_id)
                if role_object:
                    role_name = role_object.name
                    valid_pairs.append((role_name, emoji))
            else:
                # Check if role name exists
                if discord.utils.get(ctx.guild.roles, name=role):
                    valid_pairs.append((role, emoji))

    # Create a message with role reaction instructions
    instructions = "React to this message to assign yourself a role!\n\n"
    for role_name, emoji in valid_pairs:
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        instructions += f"React with {emoji} to assign the {role_name} role.\n"

    message = await ctx.send(instructions)

    # Add reactions corresponding to each selected role and emoji
    for role_name, emoji in valid_pairs:
        await message.add_reaction(emoji)

    # Function to handle reaction events
    async def reaction_handler(reaction, user):
        if user == client.user:
            return
        if reaction.message == message and reaction.emoji in [emoji for _, emoji in valid_pairs]:
            role_name = next(role for role, emoji_pair in valid_pairs if emoji_pair == reaction.emoji)
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                await user.add_roles(role)
                await user.send(f"You've been assigned the role: {role.name}")

    # Wait for reactions and call the reaction_handler function
    client.add_listener(reaction_handler, name="on_reaction_add")



@client.command(name='tempvoice', description='Create temporary voice channels that automatically delete after a period of inactivity.')
async def tempvoice(ctx):
    # Create the temporary voice channel
    new_channel = await ctx.guild.create_voice_channel(name="Temporary Channel")

    # Set permissions for the new channel
    await new_channel.set_permissions(ctx.guild.default_role, connect=True, speak=True)

    # Inform the user about the created channel
    await ctx.send(f"A temporary voice channel has been created: {new_channel.mention}. This channel will automatically delete after a period of inactivity.")

    # Define a background task to check channel activity
    async def check_activity():
        while True:
            # Wait for 5 minutes
            await asyncio.sleep(150)

            # Check if there are any members connected to the channel
            if not new_channel.members:
                # Delete the channel if no one is connected
                await new_channel.delete()
                break  # Exit the loop once the channel is deleted

    # Start the background task
    client.loop.create_task(check_activity())



