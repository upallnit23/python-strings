#Assignment: Python Strings

#1. Product Review Analysis

#Task 1: Keyword Highlighter

"""Pseudocode - 
Step 1 - use split() to separate reviews.  
Step 2 - 
Step 3 - use the if...in loop to search for key words.  
Step 4 - use upper() to capitalize key words
Step 5 - """

reviews = [ "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]

upreviews = " ".join([word for word in reviews])
print(upreviews)

for word in upreviews:
    upreviews2 = upreviews.split(" ")
print(upreviews2)

"""upreviews2 = ""

for words2 in reviews:
    upreviews2 += words2
print(upreviews2)
"""
#upreviews3 = [word.lower() for word in upreviews2]
#print(upreviews3)

upreviews3 = ""

for words3 in upreviews2:
    upreviews3 += words3.lower()
print(upreviews3)

upreviews4 = ""

for word in upreviews2:
    if word in upreviews2 == "good":
        upreviews4 = word.upper()
    elif word in upreviews2 == "bad":
        upreviews4 = word.upper()
    elif word in upreviews2 == "excellent":
        upreviews4 = word.upper()
    elif word in upreviews2 == "average":
        upreviews4 = word.upper()
    elif word in upreviews2 == "poor":
        upreviews4 = word.upper()
    else:
        upreviews4 = upreviews
upreviews4 = "".join(upreviews4)
print(upreviews4)

"""
for i, word in enumerate(upreviews3):
    if word in upreviews3[i] == "good.":
        upreviews4[i] = word.upper()
    elif word in upreviews3[i] == "bad":
        upreviews4[i] = word.upper()
    elif word in upreviews3[i] == "excellent.":
        upreviews4[i] = word.upper()
    elif word in upreviews3[i] == "average.":
        upreviews4[i] = word.upper()
    elif word in upreviews3[i] == "poor":
        upreviews4[i] = word.upper()
    else:
        upreviews4 = upreviews3
upreviews4 = " ".join(upreviews3)
print(upreviews4)
"""
#Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
"""
pwords = " ".join([word for word in positive_words])
#print(pwords)

nwords = " ".join([word for word in negative_words])
#print(nwords)

for word in range(len(pwords)):
    poswords = pwords.split()
print(poswords)

for word in range(len(nwords)):
    negwords = nwords.split()
print(negwords)
"""
poswords = ""
negwords = ""

for words in positive_words:
    poswords += words + " "
print(poswords)

for words1 in negative_words:
    negwords += words1 + " "
print(negwords)

poscount = 0
negcount = 0

for word1 in upreviews2:
        if word1 in poswords:
            poscount += 1
           
        elif word1 in negwords:
            negcount += 1
            
        else:
            continue


print(f"There are {poscount} positive keywords in the reviews.")
print(f"There are {negcount} negative words in the reviews.")

#Task 3. Review Summary

i = 0
sumreviews = []
while i != 30:
    sumreviews += upreviews4[i]
    i += 1
sumreviews += "..."
sumreviews1 = "".join(sumreviews)
print(sumreviews1)





