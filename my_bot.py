from secret import swear_list
import random
import main
bot_choice = None
user_choice = None
result = None
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
    trigger_word = [
   "bot",
   "calc",
   "good at driving",
   "riddle",
   "yell this: ",
   "ping ",
   "you suck",
   "u suck",
   "your a bad bot",
   "deebs",
   "you know what else is massive?",
   "what is massive?",
   "help"
] + swear_list
    for word in trigger_word:
       if word in user_message:
          return True
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):

  if len(user_message) >= 50:
    return "wow, thats a long message, can you shorten that for me? ;)"
  elif any(swear in user_message for swear in swear_list):
    return "hey thats not very nice. please refrain from using that language"
  elif "deebs" in user_message:
     return "deebs me timbers" # inside joke with friends (using this bot in other servers)
  elif "calc" in user_message:
    return "calc is short for calculator"
  elif "good at driving" in user_message:
     if "I" in user_message:
        return "yes"
     else:
        return ":shrug:"
  elif "riddle" in user_message:
     return random.choice([
        "What has to be broken before you can use it? ||An Egg!||",
        "What has hands but can't clap? ||A Clock!||",
        "The more you take, the more you leave behind. What am I? ||Footsteps!||",
        "I'm tall when I'm young and short when I'm old. What am I? ||A Candle||",
        "I fly without wings, I cry without eyes. What am I? ||A Cloud!||"
     ])
  elif "yell this: " in user_message:
     yelled_message = user_message[11:].upper()
     return yelled_message
  elif "ping " in user_message:
     ptp = (user_message[5:] + " ") * 50
     return ptp
  elif "you suck" in user_message or "u suck" in user_message:
     return f'I think you meant to say "{user_message.replace("suck","are the best :star_struck:")}"'
  elif "your a bad bot" in user_message:
     return f'I think you meant to say "{user_message.replace("a bad bot","an amazing bot :star_struck:")}"'
  elif "you know what else is massive?" in user_message or "what is massive?" in user_message:
     return "imagine if ninja got a LOOOOOOOOWWWWWWWWW TAAAAAPPPPEEERRRR FADDDDDDEEEEEEEE"
  elif "help" in user_message:
     return """here is my command list. have fun!
   - if you swear the bot will get mad. b/c this is a school setting you can use the word "flip" instead of an actual swear word
   - hi bot
   - calc
   - "good at driving" (try asking if someone is good at driving)
   - riddle
   - ping @(user)
   - you suck (talking to the bot)
   - your a bad bot
   - what is massive?
   - yell this: (message to yell)
"""
  else:
    return f"what's up, {user_message.replace("bot", user_name)}"





# attempt to make rock paper scissors (did not work and cant figure it out)

  # for word in rps_command:
  #   if word in user_message:
  #     bot_choice = random.choice(["rock", "paper", "scissors"])
  #     if "rrock" in user_message:
  #         user_choice = "rock"
  #     elif "ppaper" in user_message:
  #       user_choice = "paper"
  #     elif "sscissors" in user_message:
  #       user_choice = "scissors"
  #     elif "rock paper scissors" in user_message:
  #       "Please add the first letter twice to play (ex. rrock to choose rock)"
  #     else:
  #       return "try again :/"

  #     if bot_choice == user_choice:
  #         result = "I win, haha"
  #     elif bot_choice == "rock" and user_choice == "paper":
  #         result = "you win, nice"
  #     elif bot_choice == "rock" and user_choice == "scissors":
  #         result = "I win haha"
  #     elif bot_choice == "paper" and user_choice == "rock":
  #         result = "I win haha"
  #     elif bot_choice == "paper" and user_choice == "scissors":
  #         result = "you win, nice"
  #     elif bot_choice == "scissors" and user_choice == "rock":
  #       result = "you win, nice"
  #     elif bot_choice == "scissors" and user_choice == "paper":
  #       result = "I win haha"

  #     return f"you chose {user_choice}, and i chose {bot_choice}. {result}"