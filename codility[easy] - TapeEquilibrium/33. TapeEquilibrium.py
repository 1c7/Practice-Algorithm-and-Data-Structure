#-*- utf-8 -*-
# write your code in Python 2.7

def solution(A):
    a_len = len(A)
    
    #corner case
    if a_len == 1:
      return False
    elif a_len == 2:
      return False
    
    # regular case
    minimal_difference = 0
    for i in range(1, a_len):
        first_part = A[:i]
        second_part = A[i:]
        F_p_sum = sum(first_part)
        S_p_sum = sum(second_part)
        ABS_F_p_sum = abs(F_p_sum)
        ABS_S_p_sum = abs(S_p_sum)
        diff = abs(ABS_F_p_sum - ABS_S_p_sum)
        if i == 1:
            minimal_difference = diff
        elif diff < minimal_difference:
            minimal_difference = diff
    return minimal_difference
    
    
    
    
'''  
  
  
 差的地方   
    
    
    
    
    
'''
    
    

