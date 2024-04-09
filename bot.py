from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the command to start the process
def add_member(update: Update, context: CallbackContext):
    # Check if the command includes a username or user ID
    if context.args:
        user_info = context.args[0]
        
        # Add member to the group
        try:
            chat_id = update.message.chat_id
            admins = context.bot.get_chat_administrators(chat_id)
            if update.message.from_user.id in [admin.user.id for admin in admins]:
                users_count = context.bot.get_chat_members_count(chat_id)
                if users_count + len(context.args) > 100:
                    update.message.reply_text(f"Failed to add member {user_info}: The group limit of 100 members exceeded.")
                    return
                context.bot.send_message(chat_id, f"/invite {user_info}")  # Send invitation message to the user
                update.message.reply_text(f"Invitation sent to {user_info}!")
            else:
                update.message.reply_text("You don't have permission to add members to this group.")
        except Exception as e:
            update.message.reply_text(f"Failed to add member {user_info}: {e}")
    else:
        update.message.reply_text("Please provide the username or user ID of the member you want to add.")

def main():
    # Set up the bot
    updater = Updater("6811749953:AAGdD19D6gJBAhyIATWKIai4S23so3BHXBc", use_context=True)
    dp = updater.dispatcher

    # Command to trigger adding a member
    dp.add_handler(CommandHandler("addmember", add_member))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
