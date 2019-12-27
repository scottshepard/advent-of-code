input = 33100000

divisors <- function(x) {
  #  Vector of numberes to test against
  y = seq_len( ceiling( x / 2 ) )
  #  Modulo division. If remainder is 0 that number is a divisor of x so return it
  c(y[ x%%y == 0 ], x)
}

# Part 1
# R takes a long time so start close to the answert to save time
i = 776000
X = 0
while(X < input) {
  i = i + 1
  D = divisors(i)
  X = sum(D) * 10
}
print(i)

# Part 2
X = 0
i = 776000
while(X < input) {
  i = i + 1
  D = divisors(i)
  X = sum(D[i / D <= 50]) * 11
}
print(i)
