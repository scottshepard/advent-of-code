library(ggplot2)
library(plyr)

houses <- readLines("data.txt")
houses <- as.list(strsplit(houses, "")[[1]])

directionVector <- function(direction) {
  if(direction == "v") {
    c(x=0, y=-1)
  } else if(direction == ">") {
    c(x=1, y=0)
  } else if(direction == "<") {
    c(x=-1, y=0)
  } else if(direction == "^") {
    c(x=0, y=1)
  } else {
    NULL
  }
}

direction_matrix <- ldply(houses, directionVector)
direction_matrix$X <- cumsum(direction_matrix$x)
direction_matrix$Y <- cumsum(direction_matrix$y)

# Find the number of unique coordinates
sum(! duplicated(direction_matrix[, c("X", "Y")]))

# Draw a map of the houses visited by Santa
direction_matrix$color <- sample(c("RED", "GREEN"), size=nrow(direction_matrix), replace=T)
ggplot(direction_matrix, aes(x=X, y=Y, color=color)) + geom_point() +
  scale_color_manual(values=c("#d42426", "#3C8D0D")) +
  theme(axis.title=element_blank(), legend.position="none") +
  ggtitle("Map of Houses Santa Visits")


