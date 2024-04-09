from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Dictionary to store when to add each member
member_add_times = {}

# Define the command to start the process
def add_members(update: Update, context: CallbackContext):
    usernames = context.args[0].split(',')
    
    for username in usernames:
        # Add username and current time + 60 seconds to the dictionary
        member_add_times[username] = time.time() + 60  # Changed delay time to 60 seconds
        
    update.message.reply_text("Usernames added. Members will be added after 60 seconds.")

# Function to check and add members at the designated times
def check_members(context: CallbackContext):
    current_time = time.time()
    
    for username, add_time in member_add_times.items():
        if current_time >= add_time:
            # Placeholder logic to add member to a group using Telegram API
            # You should implement the actual logic here
            
            # After adding the member, you can remove them from the dictionary
            del member_add_times[username]
            print(f"Added member: {username}")

def main():
    # Set up the bot
    updater = Updater("6811749953:AAGdD19D6gJBAhyIATWKIai4S23so3BHXBc", use_context=True)
    dp = updater.dispatcher

    # Command to trigger adding the members
    dp.add_handler(CommandHandler("addmembers", add_members))

    # Start the bot
    updater.start_polling()
    
    # Set up a job to check and add members periodically
    updater.job_queue.run_repeating(check_members, interval=1, first=0)

    updater.idle()

if __name__ == '__main__':
    main()
