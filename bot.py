import discord
import random

# Function to handle user messages and generate responses
def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hi there!'
    elif p_message == 'roll':
        return str(random.randint(1, 6))
    elif p_message == '!help':
        return "This is a help message that you can modify."
    elif p_message == 'hi':
        return 'How can I help you?'
        
    else:
        return "Yeah, I don't know. Try typing '!help'."

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
        
        # Send the response to the mobile device
        # Replace the following line with the code to send the response to your mobile device
        send_to_mobile(response)
        
    except Exception as e:
        print(e)

# Main function to run the Discord bot
def run_discord_bot():
    TOKEN = 'Token HERE'
    intents = discord.Intents.default()
    intents.typing = False

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Run the bot with your Discord token
    client.run(TOKEN)

# Function to send response to your mobile device
def send_to_mobile(response):
    # Add your code to send the response to your mobile device
    # This can be using push notifications, messaging services, or any other method of your choice
    # Replace this placeholder function with your actual implementation
    print("Sending response to mobile:", response)

# Run the Discord bot
run_discord_bot()
