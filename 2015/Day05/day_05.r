strings <- readLines("data.txt")

# Part 1
containsThreeVowels <- function(s) {
  # Not three distinct vowels
  grepl("(.*[aeiou]){3}", s)
}

oneLetterTwiceInARow <- function(s) {
  # Any letter that appers twice in a row
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

sum(sapply(strings, isStringNice1))

# Part 2
letterPairAppearsTwice <- function(s) {
  # Any pair of letters that appear twice at some point in the string without 
  # overlapping
  # i.e xyxy (xy) but not aaa (aa) but middle a is used twice
  
  # First find all two-letter pairs
  str_split <- strsplit(s, "")[[1]]
  if(length(str_split) <= 2) 
    return(FALSE)
  pairs <- sapply(2:length(str_split), function(i) paste0(str_split[i], str_split[i-1]))
  # Exclude those that happen sequentially
  bool_vec <- sapply(seq_along(pairs), function(i) {
    if(i == 1) {
      TRUE
    } else {
      pairs[i] != pairs[i-1]
    }
  })
  bool_vec <- sapply(seq_along(bool_vec), function(i) {
    if(i == 1) {
      bool_vec[i]
    }
    else if(bool_vec[i] == F && bool_vec[i-1] == F) {
      bool_vec[i] <- T
    } else {
      bool_vec[i]
    }
  })
  pairs <- pairs[bool_vec]
  any(table(pairs) >= 2)
}

oneLetterRepeatsWithOneLetterSeparation <- function(s) {
  # A three letter sandwich where the bread is the same letter
  # i.e. xyx, efe, or aaa
  str_split <- strsplit(s, "")[[1]]
  any(sapply(unique(str_split), function(char) {
    indicies <- c(gregexpr(char, s)[[1]])
    any(sapply(indicies, function(i) abs(indicies - i)) == 2)
  }))
}

isStringNice2 <- function(string) {
  letterPairAppearsTwice(string) && oneLetterRepeatsWithOneLetterSeparation(string)
}

sum(sapply(strings, isStringNice2))
