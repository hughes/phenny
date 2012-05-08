import cleverbot
mycb = cleverbot.Session()
def talk(phenny, input):
	result = mycb.Ask(input[11:])
        phenny.reply(result)
talk.rule = r'$nickname:'
talk.priority = 'low'
talk.thread = False
