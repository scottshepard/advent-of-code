library(stringr)
library(permute)
library(plyr)

distances <- readLines("data.txt")

cities <- str_extract_all(distances, "[A-Z][:alpha:]+")
cities <- unique(unlist(cities))

distance <- function(city1, city2) {
  if(city1 == city2) {
    NA
  } else {
    line <- distances[grepl(city1, distances) & grepl(city2, distances)]
    as.numeric(str_extract(line, "[:digit:]+"))
  }
}

perms <- allPerms(1:8, control=how(maxperm = 362881))

routeDistance <- function(route_order) {
  route <- cities[route_order]
  sum(sapply(1:7, function(i) {
    distance(route[i], route[i+1])
  }))
}

route_distances <- apply(perms, 1, routeDistance)

# Part 1
min(route_distances)
# Answer is 141

# Part 2
max(route_distances)
# Answer is 736s