def hugs(phenny, input):
    phenny.do("hugs %s" % input.nick)

hugs.rule = r'ACTION hugs $nickname'
hugs.priority = 'low'
hugs.thread = False
