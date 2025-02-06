from secret import swear_list
import random
rps_ans = None

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "bot" in user_message:
      return True
  elif swear_list in user_message:
      return True
  elif "calc" in user_message:
      return True
  elif "rock paper scissors" in user_message:
      return True
  elif "cheater" in user_message:
      return True
  else:
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
  elif swear_list in user_message:
    return "hey thats not very nice. please refrain from using that language"
  elif "calc" in user_message:
    return "calc is short for calculator"
  elif "rock paper scissors" in user_message:
    return f"ok let me think... i pick {random.choice(["rock", "paper", "scissors"])}"
  elif "cheater" in user_message:
    return ":shrug:"
  else:
    return f"what's up, {user_message.replace("bot", user_name)}"