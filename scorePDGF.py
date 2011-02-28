#!/usr/bin/python
"""A command line script for scoring games of paranoid debate.

A description of the game and the file format for running the scoring
algorithm can be found on the web.

http://wiki.lesswrong.com/wiki/Paranoid_debating

Released to the public domain I guess?

Authors:
Jennifer Rodriguez-Mueller
Steve Rayhawk
"""
import math

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
            advisors = filter(len,people[1].split(","))
            tricksys = filter(len,people[2].split(","))
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
        logarithmic = True
        if (logarithmic):
            low = math.log(nums[1])
            high = math.log(nums[2])
            actual = math.log(nums[3])
        else:
            low = nums[1]
            high = nums[2]
            actual = nums[3]
        center = (low+high)/2.0
        
        ## <Thank you Steve>
        #
        # Compute Cauchy inverse cdf of
        #    q = 1/2 + confidence/2
        # (high quantile of centered confidence interval)
        #    as tan((q-1/2)*pi)
        scale = math.tan(confidence/2.0*math.pi)*(high-low)/2.0
        # Compute Cauchy pdf as 1/(1+x**2)/pi
        density = 1.0/(1+((actual-center)/scale)**2)/math.pi/scale
        # Calculate scores round by round...
        speakerScore = math.log(density) * 2.0
        advisorScore = math.log(density)
        tricksyScore = math.log(density) * -1.0
        ## </You're welcome Jennifer>
        
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
        print "USAGE: cat paranoidDebateGameFile | ",sys.argv[0],"\n"
        print "Problem with scoring script or game file... look for help."
        print "http://wiki.lesswrong.com/wiki/Paranoid_debating"
