import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        user = message.author
        await message.delete()
        if response[0] == 1:
            role1 = discord.utils.get(user.guild.roles, name=response[1])
            role2 = discord.utils.get(user.guild.roles, name=response[2])
            print(role1)
            print(role2)
            if user.get_role(role1.id) != None:
                print("tem")
                await user.add_roles(role2)
                await user.remove_roles(role1)
                await user.send("Resposta Correta.")
            else:
                print("nao tem")
                await user.send("Resposta incorreta.")
        else:
            await user.send("Resposta Incorreta.")
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        await send_message(message, user_message)

    client.run(TOKEN)
