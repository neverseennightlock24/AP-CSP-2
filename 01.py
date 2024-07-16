# Unit 3 Application Question
# [Insert Name]
import time
import random

blockPair = {}
blockList = ["A"]
blockList2 = []
courses = ["ICS3UN01", "ICS3UN02", "ICS3UN03", "MCR3UE01"]

# Giving the program time to process requests so as to run everything smoothly; implemented after a cpu overflow
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(0.5)

# Randomly but orderly selecting possible following blocks after block A as defined by blockList
arbitNum = random.randint(1,2)
if arbitNum == 1:
  blockList.append("A")
  arbitNum2 = random.randint(1,2)
  if arbitNum2 == 1:
    blockList.append("A")
    arbitNum4 = random.randint(1,2)
    if arbitNum4 == 1:
      blockList.append("A")
    if arbitNum4 == 2:
      blockList.append("B")
  if arbitNum2 == 2:
    blockList.append("B")
    arbitNum5 = random.randint(1,2)
    if arbitNum5 == 1:
      blockList.append("B")
    if arbitNum5 == 2:
      blockList.append("C")
    
if arbitNum == 2:
  blockList.append("B")
  arbitNum3 = random.randint(1,2)
  if arbitNum3 == 1:
    blockList.append("B")
    arbitNum6 = random.randint(1,2)
    if arbitNum6 == 1:
      blockList.append("B")
    if arbitNum6 == 2:
      blockList.append("C")
  if arbitNum3 == 2:
    blockList.append("C")
    arbitNum7 = random.randint(1,2)
    if arbitNum7 == 1:
      blockList.append("C")
    if arbitNum7 == 2:
      blockList.append("D")

# Taking in user input for the arbitrary number of course-block pairs, as informed when clarification was requested by peers who asked the course instructor
while True:
  try:
    userInput = int(input("Enter a number from 1-4, representing the number of courses present: \n"))
    assert 0 < userInput < 5
    print("\nNow running the block-pair simulator: ")
    # Setting a sleep timer to prevent a RAM overflow
    time.sleep(1.5)
    countdown(3)
  except ValueError:
    print("Not an integer! Please enter an integer.")
  except AssertionError:
    print("Please enter an integer between 1 and 4. ")
  else:
    break

# A function to pair the preselected courses to blocks
def pairing(**kwargs):
  for i in range(userInput):
    blockPair[courses[i]] = blockList[i]
  print(blockPair)

pairing()

# Extracting the possibly reduced, depending on userInput, key pair values from the blockPair dictionary
for key, value in blockPair.items():
  blockList2.append(value)

# This function take the most frequently-occuring block from blockList2 and returns it. In the case of a tie, either will be returned
# It doesn't matter since all we're looking for is the amount of occurrences returned to us
def minTeachers(**kwargs):
  counter = 0
  for i in blockList2:
    valueFreq = blockList2.count(i)
    if (valueFreq > counter):
      counter = valueFreq
      num = i
      
  return num 

time.sleep(1.5)

# Finally, this counts and prints the amount of times the most frequent letter, as determined by minTeachers, occurs
counter = minTeachers()
print("\n∴The minimum amount of teachers required are", blockList2.count(counter))
