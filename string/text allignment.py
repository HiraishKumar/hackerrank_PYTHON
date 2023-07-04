t=int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range (0,t):
    print((c*(1+2*i)).center(t*2))    
#Top Pillars
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*6))
#Middle Beam
for i in range((t+1)//2):
    print((c*(t*5)).center(t*6))
#Bottom Pillars
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*6))
#Bottomcone
for i in range(0,t):
    print((c*(t*2-1-2*i)).center(t*10))

'''Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

Constraints

The thickness must be an odd number.

Output Format

Output the desired logo.

Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H '''