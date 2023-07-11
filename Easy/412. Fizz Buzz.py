#Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        answer=list(range(1,n+1))
        for i in range(n):
            if answer[i]%15==0:
                answer[i]="FizzBuzz"
            elif answer[i]%5==0:
                answer[i]="Buzz"
            elif answer[i]%3==0:
                answer[i]="Fizz"
            else:
                answer[i]=str(answer[i])
        return(answer)
