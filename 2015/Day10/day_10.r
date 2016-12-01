


lookAndSay <- function(s) {
  s <- as.character(s)
  b <- breaks(s)
  counts <- counts(s, b)
  paste0(unlist(lapply(seq_along(counts), function(i) {
    c(counts[i], names(counts[i]))
  })), collapse="")
} 


breaks <- function(s) {
  s <- strsplit(s, "")[[1]]
  if(length(s) == 1) {
    1
  } else {
    c(1, unlist(sapply(2:length(s), function(i) {
      if(s[i] != s[i-1]) i
    })))
  }
}

counts <- function(s, b) {
  s <- strsplit(s, "")[[1]]
  sapply(seq_along(b), function(i) {
    if(i == length(b)) {
      table(s[b[i]:length(s)])
    } else {
      table(s[b[i]:(b[i+1]-1)])
    }
  })
}

# Part 1
input <- "1113122113"
sapply(1:40, function(i) {
  input <<- lookAndSay(input)
})
nchar(input)
# Answer is 360154

# Part 2
input <- "1113122113"
sapply(1:50, function(i) {
  input <<- lookAndSay(input)
  print(i)
})
nchar(input)
# Answer is 5103798