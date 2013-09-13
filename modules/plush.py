import random


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


adverbs = [
    "carefully",
    "correctly",
    "cautiously",
    "eagerly",
    "happily",
    "loudly",
    "patiently",
    "quickly",
    "quietly"
]


def purrs(phenny, input):
    phenny.do("purrs " + random.choice(adverbs))

purrs.rule = r'ACTION pets $nickname'
purrs.priority = 'low'
purrs.thread = False
