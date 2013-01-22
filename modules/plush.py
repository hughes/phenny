def hugs(phenny, input):
    phenny.do("hugs %s" % input.nick)

hugs.rule = r'ACTION hugs $nickname'
hugs.priority = 'low'
hugs.thread = False


def kicks(phenny, input):
    phenny.say('ow!')

kicks.rule = r'ACTION kicks $nickname'
kicks.priority = 'low'
kicks.thread = False
