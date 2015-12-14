library(ggplot2)
library(dplyr)

houses <- readLines("data.txt")
houses <- as.list(strsplit(houses, "")[[1]])

# Part 1
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

direction_matrix <- plyr::ldply(houses, directionVector)
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

# Part 2
direction_matrix$santa <- c("Santa", "Robo-Santa")
santa <- filter(direction_matrix, santa == "Santa")
robosanta <- filter(direction_matrix, santa == "Robo-Santa")
santa$X <- cumsum(santa$x)
santa$Y <- cumsum(santa$y)
robosanta$X <- cumsum(robosanta$x)
robosanta$Y <- cumsum(robosanta$y)
santas_matrix <- rbind(santa, robosanta)

sum(! duplicated(santas_matrix[, c("X", "Y")]))

ggplot(santas_matrix, aes(x=X, y=Y, color=santa)) + geom_point() +
  scale_color_manual(values=c("#d42426", "#3C8D0D")) +
  theme(axis.title=element_blank()) +
  ggtitle("Map of Houses Santa & Robo-Santa Visits")
