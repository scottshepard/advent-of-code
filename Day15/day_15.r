library(stringr)

ingredients <- readLines("data.txt")
df <- read.csv("combos.csv")
teaspoons <- 100

ingredients <- plyr::ldply(ingredients, function(ingredient) {
  data.frame(
    name = str_extract(ingredient, "[:alpha:]+"),
    capacity = as.numeric(str_extract(ingredient, "(?<=capacity )-?[:digit:]")),
    durability = as.numeric(str_extract(ingredient, "(?<=durability )-?[:digit:]")),
    flavor = as.numeric(str_extract(ingredient, "(?<=flavor )-?[:digit:]")),
    texture = as.numeric(str_extract(ingredient, "(?<=texture )-?[:digit:]")),
    calories = as.numeric(str_extract(ingredient, "(?<=calories )-?[:digit:]"))
  )
})

cookieScore <- function(tsps, IM = ingredients, max_cal = NULL) {
  if(!is.null(max_cal)) {
    if(sum(IM$calories * tsps) != 500 )
      return(NULL)
  }
  
  IM$capacity <- IM$capacity * tsps
  IM$durability <- IM$durability * tsps
  IM$flavor <- IM$flavor * tsps
  IM$texture <- IM$texture * tsps
  
  scores <- apply(as.matrix(IM[, c("capacity", "durability", "flavor", "texture")]), 2, sum)
  if(any(scores < 0)) scores[scores < 0] <- 0
  prod(scores)
}

l <- sapply(1:nrow(df), function(i) {
  cookieScore(c(t(df[i, ])))
})
max(unlist(l))
# Answer is 13882464

# Part 2, 500 calories only

l500 <- sapply(1:nrow(df), function(i) {
  cookieScore(c(t(df[i, ])), max_cal = 500)
})
max(unlist(l500))
# Answer is 11171160
