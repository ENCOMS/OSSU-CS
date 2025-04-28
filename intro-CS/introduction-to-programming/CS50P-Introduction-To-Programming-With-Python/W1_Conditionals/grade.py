
score = int(input("Score: "))


#first approach: Not optimize
"""
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 89:
    print("Grade: B")
elif score >= 70 and score < 79:
    print("Grade: C")
elif score >= 60 and score < 69:
    print("Grade: D")
else:
    print("Grade: F")

#This code do as intended, but we could asking the questions if we can do better, tight, efficient code, we can do some changes.
"""

#Second approach: Tight and aesthetic more hand like approach. Python allows us to nest the conditional if evaluation the same variable against other values.
"""    
if  90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 89:
    print("Grade: B")
elif 70 <= score < 79:
    print("Grade: C")
elif 60 <= score < 69:
    print("Grade: D")
else:
    print("Grade: F")
""" 

#Third approach: Thinking how we can improve this, we can eliminated the two questions of lower and higher range and simplified to use only the lower range, as if greater than the lower range is in the range of the score and if greater than next lower score is another grade until all is evaluated. This way is more tight, small and hopefully endure the time.
    
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


