list <- readLines("data.txt")

# String characters
n_char_string <- nchar(list)

n_char_memory <- sapply(seq_along(list), function(i) {
  nchar(eval(parse(text=list[i])), type="bytes")
})

# Part 1
sum(n_char_string) - sum(n_char_memory)
# Answer is 1350

# Part 2
sum(nchar(sapply(list, deparse))) - sum(n_char_string)

