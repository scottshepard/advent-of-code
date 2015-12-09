containsThreeVowels <- function(s) {
  # Not three distinct vowels
  grepl("(.*[aeiou]){3}", s)
}

oneLetterTwiceInARow <- function(s) {
  grepl("(.)\\1", s)
}

noNaughtyCombo <- function(s) {
  # Checks string s if it contains any naughty combo
  !any(sapply(c("ab", "cd", "pq", "xy"), grepl, s))
}

isStringNice1 <- function(string) {
  #' A nice string is one with all of the following properties:
  #' 1. It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
  #' 2. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
  #' 3. It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
  containsThreeVowels(string) && oneLetterTwiceInARow(string) && noNaughtyCombo(string) 
}

strings <- readLines("data.txt")

# Part 1
sum(sapply(strings, isStringNice1))


