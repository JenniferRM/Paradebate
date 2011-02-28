#!/usr/bin/python
"""A command line script for scoring games of paranoid debate.

A description of the game and the file format for running the scoring
algorithm can be found on the web.

http://wiki.lesswrong.com/wiki/Paranoid_debating

Released to the public domain I guess?

Authors:
Jennifer Rodriguez-Mueller
??
"""

def main():
    """Handle job of "being a script" from command line."""
    import sys
    scores = scoreParanoidDebatingGameFile(sys.stdin)
    for person in scores:
        print "The score of",person,"was",round(scores[person],3)

def scoreParanoidDebatingGameFile(inFileObj):
    """Score a game of paranoid debating in PDGF.  Callable from IDLE :)"""
    scores = {}
    for rawline in inFileObj:
        # Incremental file parsing...
        line = rawline.strip()
        if not line:
            continue
        if line[0] == "#":
            continue
        try:
            oneRound = line.split("\t")
            nums = []
            for i in [0,1,2,3]:
                nums.append(float(oneRound[i]))
            people = oneRound[4].split("|")
            speaker = people[0]
            advisors = people[1].split(",")
            tricksys = people[2].split(",")
        except:
            Exception("Bad format!")
        for person in advisors+tricksys+[speaker]:
            if person.lower() not in scores:
                scores[person.lower()] = 0.0
        if nums[0] < 0.0 or 1.0 < nums[0]:
            Exception("Illegal confidence interval")
        confidence = nums[0]
        if nums[1] > nums[2]:
            Exception("Probable confusion about bounds...")
        correct = True
        if nums[3] < nums[1] or nums[2] < nums[3]:
            correct = False
        # Calculate scores round by round...
        if correct:
            speakerScore = confidence * 2.0
            advisorScore = confidence
            tricksyScore = 0
        if not correct:
            speakerScore = confidence * -1.0
            advisorScore = 0
            tricksyScore = confidence * 2.0

        # Update scores as you go...
        scores[speaker.lower()] += speakerScore
        for person in advisors:
            scores[person.lower()] += advisorScore
        for person in tricksys:
            scores[person.lower()] += tricksyScore
    return scores

if __name__ == '__main__':
    import sys
    try:
        main()
    except:
        print "USAGE: cat paranoidDebateGameFile |"sys.argv[0],"\n"
        print "Problem with scoring script or game file... look for help."
        print "http://wiki.lesswrong.com/wiki/Paranoid_debating"
