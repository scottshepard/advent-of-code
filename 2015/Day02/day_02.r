presents <- readLines("data.txt")

# Part 1
wrappingPaperNeeded <- function(l, w, h) {
  smallest_side <- min(c(l*w, w*h, h*l))
  2*l*w + 2*w*h + 2*h*l + smallest_side
}

presents <- strsplit(presents, "x")

wrapping_area <- sapply(presents, function(present) {
  pdims <- as.numeric(present)
  wrappingPaperNeeded(pdims[1], pdims[2], pdims[3])
})

sum(wrapping_area)
# Answer is 1588178 square feet of wrapping paper

# Part 2
ripponNeeded <- function(l, w, h) {
  smallest_two_sides <- c(l, w, h)[order(c(l, w, h))][c(1,2)]
  sum(smallest_two_sides * 2) + l*w*h
}

ribbon_length <- sapply(presents, function(present) {
  pdims <- as.numeric(present)
  ripponNeeded(pdims[1], pdims[2], pdims[3])
})

sum(ribbon_length)
# Answer is 3783758 feet of ribbon