library(stringr)

letter_straights <- paste0(sapply(0:23, function(i) {
  paste0(letters[1:3+i], collapse="")
}), collapse = "|")

letter_pairs <- paste(sapply(letters, function(l) {
  paste(rep(l, 2), collapse="")
}), collapse="|")

nextGoodPassword <- function(pwd) {
  password_is_bad <- TRUE
  i <- 1
  while(password_is_bad) {
    pwd <- incrementPassword(pwd)
    password_is_bad <- ! isGoodPassword(pwd)
    i <- i + 1
    if((i-1) %% 30000 == 0) print(paste(i, ":", pwd))
  }
  pwd
}

isGoodPassword <- function(pwd) {
  # A straight of three letters 
  grepl(letter_straights, pwd) &&
    # Don't contain i, o or l
  ! grepl("i|l|o", pwd) &&
    # Two different, non-overlapping pairs of letters
  length(unlist(gregexpr(letter_pairs, pwd))) >= 2
}

incrementPassword <- function(pwd, pwd_i = length(pwd)) {
  if(grepl("i|l|o", pwd)) {
    badLetterIncrement(pwd)
  } else {
    pwd <- unlist(strsplit(pwd, ""))
    pwd[pwd_i] <- nextLetter(pwd[pwd_i])
    if(pwd[pwd_i] == "a") {
      pwd <- incrementPassword(pwd, pwd_i-1)
    }
    paste(pwd, collapse="")
  }
}

badLetterIncrement <- function(pwd) {
  loc1 <- regexpr("i|l|o", pwd)[[1]]
  pwd <- unlist(strsplit(pwd, ""))
  if(loc1 == length(pwd)) {
    pwd[length(pwd)] <- nextLetter(pwd[length(pwd)])
  } else {
    pwd[loc1] <- nextLetter(pwd[loc1])
    pwd[(loc1+1):length(pwd)] <- "a"
  }
  paste(pwd, collapse = "")
}

nextLetter <- function(letter) {
  i <- which(letter == letters) + 1
  if(i == 27) i <- 1
  letters[i]
}

last <- function(vec) {
  vec[length(vec)]
}

# Part 1
nextGoodPassword("vzbxkghb")
# Answer is vzbxxyzz

# Part 2
nextGoodPassword(nextGoodPassword("vzbxkghb"))
# Answer is vzcaabcc