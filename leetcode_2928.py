#initialize the distribution function

def fn_distribute_candies(n,limit):
  # initialize the number of ways
  cnt = 0
  
  child_1 = limit
  # First Loop for the first child 
  for i in range(limit + 1):
    child_2 = min(limit,n-child_1)
    # Second Loop for the second child 
    for j in range(limit + 1):
      child_3 = n - child_1 - child_2
      if child_3 > limit or child_3<0:
        break
      print(child_1,child_2,child_3)
      cnt += 1
      child_2 -= 1
      if child_2 > limit or child_2<0:
        break
    child_1 -= 1
  return cnt

def fn_check_limit(n,limit):
  if (1.0*n)/limit > 3:
    print("Number of candies are more than the limit after limited distribution")
  if n < limit:
    limit = n
    #Call the distribution function
  return fn_distribute_candies(n,limit)

# Initialize the variables
n = 12
limit = 3

#Call the check function
fn_check_limit(n,limit)