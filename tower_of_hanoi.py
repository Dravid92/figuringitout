### Problem statement : 


## Goal 

# To find the number of moves required To transfer disks from A to either B or C , 

#conditions 
#1 Don't place larger disks on top of smaller disks 
#2 Move only one disk at a time .


## Mathematical equation :- 2*n - 1 moves , say n = 5 , then 2**5 - 1 = 31 moves 

## recursive method - code 

### Pseduocode - 

# Assumption - T = total number of moves 

# 1. Input : number - Number of disks 

# 2. Output : number - Number of moves required to displace the disks 

## Base case : T(0) = 0
## By mathematical induction : T(n) = 2*T(n-1) + 1 moves 

n = 5 
## 2*T(4)+1
## T(4) = 2*T(3)+1
## T(3) = 2*T(2)+1
## T(2) = 2*T(1) + 1
## T(1) = 2*0 + 1 = 1
def total_no_moves(n):
	"""
	can accept only positive numbers;
	"""
	t = 0
	if n < 0:
		raise "Cannot use negative numbers!"
	elif n == 0:
		return t
	else:
		t += 2*total_no_moves(n-1) + 1
		return t

print(total_no_moves(8))
