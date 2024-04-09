from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the command to start the process
def add_member(update: Update, context: CallbackContext):
    # Check if the command includes a username or user ID
    if context.args:
        user_info = context.args[0]
        
        # Add member to the group
        try:
            context.bot.bot_data['admins'] = context.bot.get_chat_administrators(context.job.context['chat_id'])
            context.bot.bot_data['creator'] = context.bot.get_chat(context.job.context['chat_id']).get('pinned_message').author
            if update.message.from_user.id in context.bot.bot_data['admins'] or update.message.from_user.id == context.bot.bot_data['creator']:
                context.bot.bot_data['users'] = context.bot.get_chat_members_count(context.job.context['chat_id'])
                if context.bot.bot_data['users'] + len(context.args) > 100:
                    update.message.reply_text(f"Failed to add member {user_info}: The group limit of 100 members exceeded.")
                    return
                context.bot.add_chat_members(chat_id=update.message.chat_id, user_ids=[user_info])
                update.message.reply_text(f"Member {user_info} added successfully!")
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
