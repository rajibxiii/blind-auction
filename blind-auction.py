import os
import logos

def clear ():

    os.system ("cls")
def addNewBidder ():
    print (logos.auctionRunning)
    bidderID = input ("What's your ID?: ")
    bidderName = input ("Your name?: ")
    bidPrice = float(input ("Bid Price?: "))

    newBid = {}
    newBid["bidderID"] = bidderID
    newBid["bidderName"] = bidderName
    newBid["bidPrice"] = bidPrice

    bids.append(newBid)
    clear ()
    bidContinuer () 

def bidContinuer ():
    print (logos.auctionRunning)
    continueBidding = input ("Is there any other bidder? (y/n): ")

    if (continueBidding == "y"):
        clear()
        addNewBidder ()
    elif (continueBidding == "n"):
        clear()
        print ("Thank you for participating in the auction!")
    else:
        print ("Wrong input. Please try again")
        bidContinuer ()

def printHighestBidder ():
    highestBidPrice = bids[0]["bidPrice"]
    highestBidderIndex = 0
    for i in range (1, len(bids)):
        if bids[i]["bidPrice"] > highestBidPrice:
            highestBidPrice = bids[i]["bidPrice"]
            highestBidderIndex = i

    print (f"\nThe auction winner is: {(bids[highestBidderIndex]["bidderName"]).upper()}, bidder ID: {(bids[highestBidderIndex]["bidderID"])}\nwith a bid price of {(bids[highestBidderIndex]["bidPrice"])}")


bids = []
addNewBidder()
printHighestBidder()