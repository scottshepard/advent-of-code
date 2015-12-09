presents <- readLines("data.txt")

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