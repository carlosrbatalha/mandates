# Function definition to calculate the distribution of seats
def calculateSeats(votes, seats):
    
    # Initialization of lists to store the results of each party
    partyA, partyB, partyC, partyD, allLists = [], [], [], [], []
    
    # Initializations for control of iterations
    count = 1  # Counter for dividing votes
    n = 0  # Index to access the votes of the parties
    k = seats  # Total seats to be distributed
    
    # Loop to calculate the votes divided by the counter for each party and distribute seats
    while k > 0:
        # Calculates the division result of votes by count value for each party
        resultPartyA = int(votes[n]/count)
        resultPartyB = int(votes[n+1]/count)
        resultPartyC = int(votes[n+2]/count)
        resultPartyD = int(votes[n+3]/count)
        # Adds the calculated results to the respective lists of each party
        partyA.append(resultPartyA)
        partyB.append(resultPartyB)
        partyC.append(resultPartyC)
        partyD.append(resultPartyD)
        # Increments the counter and decrements the total of seats to be distributed
        count += 1
        k -= 1

    # Adds the lists of each party to the list containing all lists
    allLists.extend([partyA, partyB, partyC, partyD])
    
    # Initialization of a list to store the sorted votes
    sortedList = []    
    number = 0
    # Iterates over all lists and their values to sort the votes
    for i in allLists:
        for y in i:
            if y > number:
                sortedList.append(y)
            else:
                continue
    
    # Sorts the list of votes in descending order
    sortedList.sort(reverse=True)
    
    # Initializes a list to store the highest votes up to the limit of seats
    topSeats = []
    countThree = 0
    
    # Selects the highest votes according to the number of available seats
    while countThree < seats:
        topSeats.append(sortedList[countThree])
        countThree += 1
      
    # Initializes lists to store the final seats of each party
    finalPartyA, finalPartyB, finalPartyC, finalPartyD = [], [], [], []
    
    # Distributes the seats to each party based on the highest votes
    for l in topSeats:
        if l in allLists[0]:
            finalPartyA.append(l)
        if l in allLists[1]:
            finalPartyB.append(l)
        if l in allLists[2]:
            finalPartyC.append(l)
        if l in allLists[3]:
            finalPartyD.append(l)
            
    # Converts the final seat lists into strings for printing
    finalStrPartyA = str(finalPartyA)[1:-1]
    finalStrPartyB = str(finalPartyB)[1:-1]
    finalStrPartyC = str(finalPartyC)[1:-1]
    finalStrPartyD = str(finalPartyD)[1:-1]
    
    # Prints the final result of the seat distribution
    print(f'Party A - {len(finalPartyA)} seats ({finalStrPartyA})') 
    print(f'Party B - {len(finalPartyB)} seats ({finalStrPartyB})') 
    print(f'Party C - {len(finalPartyC)} seats ({finalStrPartyC})') 
    print(f'Party D - {len(finalPartyD)} seats ({finalStrPartyD})')   

# Main function that starts the program
def main():
    # Defines the number of seats to be distributed
    seats = int(10)
    
    # Defines the number of votes for each party
    partyA = 2460
    partyB = 1830
    partyC = 940
    partyD = 800

    # Groups votes into a list
    votes = [partyA, partyB, partyC, partyD]
    
    # Calls the calculation function with the defined votes and seats
    calculateSeats(votes, seats)

# Checks if this is the main script and runs the program
if __name__== '__main__':
    main()
