#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0 # O(1)
    while (a < n * n * n): # loops until a = n^3, L*n^2 = n^3, L = n^3 / n^2 = n; O(n)
      a = a + n * n # increases a by n^2 each loop, a = L*n^2
```
The code will create a variable, then increase the variable by n^2 until it reaches n^3. Thus, the run-time complexity is O(n) because it will loop `n^3/n^2 = n` times.

```python
b)  sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1) * O(n) from being inside loop
      while j < n: # loop until j >= n, 2^L = n, L = log(n)/log(2); O(log n) * O(n) = O(n*log n)
        j *= 2 # j = 2^L
        sum += 1
```
The code loops through 0 to n and increments a variable log(n)/log(2) times each loop. Thus the run-time complexity is O(n\*log n) because the nested loop will run `n\*log(n)/log(2)` times.

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0: # base case: O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # repeats from n to 0 in steps of -1; O(2) * O(n) = O(2n)
```
The code recursively calls itself from n-1 to 0 in steps of -1, so it will repeat n times. It only does 2 non-intensive operations per call, so the run-time complexity is just O(n).

## Exercise II
I would start at the middle floor and throw the egg. If it breaks, I would move to the middle floor of the floors below my current floor. Otherwise, if it did not break, I would move to the middle floor of the floors above my current floor.

Then, I would once again throw the egg. If it breaks, I move to the middle floor of the floors below my current floor but above the previous floor I threw the previous egg from (if it is below me). Otherwise, if it does not break, I move to the middle floor of the floors above my current floor but below the previous floor I threw the previous egg from (if it is above me).

I would repeat the steps of the above paragraph until I reach the floor where the egg does not break but it did break on the above floor, or vice versa. Thus the final floor where the egg did not break is floor f.

The worse case scenario for the number of eggs used would be `log(n)/log(2)`, as each step rules out half the remaining floors, which gives a run-time complexity approximation of O(log n).

Although, in actuality, the egg will probably break when thrown even from the first floor. It is an egg.
