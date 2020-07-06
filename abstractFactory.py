"""
Create a product-family, consisting of several products.
A product-family builds a unit. Factory can be swapped out.
Borderlands-/Claptrap-Themed Example.
"""
import quotes as qts
import random

#Define abstract class
class Robot:

    def __init__(self):
        super(Robot, self).__init__()

    def randomQuote(self):
        pass

#Define concrete classes, inheriting from abstract class
class CL4PTP(Robot):

    def __init__(self):
        super(CL4PTP, self).__init__()

    def randomQuote(self, quote):
        return "\nClaptrap once famously said:\n"+ quote + "\n"

class SHD0TP(Robot):

    def __init__(self):
        super(SHD0TP, self).__init__()

    def randomQuote2(self, quote):
        return "5H4D0W-TP never said:\n"+ quote
    
    def worldDominationQuote(self, worldDominationQuote):
        return "\n\nBut 5H4D0W-TP may or may not have said:\n" + worldDominationQuote + "\n"

#Basic approach to create products
class StoriesFromTheBorderlands():

    def __init__(self, skin):
        self.robotType = skin

    def getCL4PTP(self):
        quote_dict={
            "usualClaptrap":CL4PTP(),
        }
        return quote_dict[self.robotType]

    def getSHD0TP(self):
        quote_dict={
            "shadowTrap":SHD0TP()
        }
        return quote_dict[self.robotType]

"""
Generating objects to test the abstract factory method. 
Get a random quote and print it to terminal for a usual Claptrap-Unit, 
then repeat for Shadow-Trap (plus a stupid world annihilation quote).
"""
normalClaptrap = StoriesFromTheBorderlands("usualClaptrap")
quoting = normalClaptrap.getCL4PTP()
randomQuote = qts.quotesList[random.randrange(0, len(qts.quotesList))]
print(quoting.randomQuote(randomQuote))

shadowTrap = StoriesFromTheBorderlands("shadowTrap")
quoting2 = shadowTrap.getSHD0TP()
randomQuote2 = qts.quotesList[random.randrange(0, len(qts.quotesList))]
crazyWorldDominationQuote = qts.shadowTrapQuote
print(quoting2.randomQuote2(randomQuote2), quoting2.worldDominationQuote(crazyWorldDominationQuote))