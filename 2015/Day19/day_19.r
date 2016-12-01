library(stringr)

MOLECULE <- readLines("input.txt")

df <- readLines("replacements.txt")
df <- data.frame(
  char = str_extract(df, "[:alpha:]+(?= =>)"),
  replacement = str_extract(df, "(?<==> )[:alpha:]+"),
  stringsAsFactors = F
)

findAllReplacements <- function(molecule, input, replacement) {
  locs <- gregexpr(input, molecule)
  if(locs[[1]] == -1) {
    NULL
  } else {
    lapply(seq_along(unlist(locs)), function(j) {
      start <- locs[[1]][j]
      paste0(
        substr(molecule, 0, start - 1), 
        replacement, 
        substr(molecule, start + attr(locs[[1]], "match.length")[j], nchar(molecule))
      )
    })
  }
}

outputs <- lapply(1:nrow(df), function(i) {
  findAllReplacements(MOLECULE, df[i, ]$char, df[i, ]$replacement)
})

outputs <- unlist(outputs)

# Part 1
dplyr::n_distinct(outputs)
# Answer is 535

