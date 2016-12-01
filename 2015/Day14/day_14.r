library(stringr)
library(dplyr)
library(reshape2)

input_seconds <- 2503

flights <- readLines("data.txt")



parseFlight <- function(flight) {
  d <- str_extract(flight, "([A-Z])([a-z]*)")
  s <- str_extract(str_extract(flight, "[:digit:]+ km/s"), "[:digit:]+")
  f <- str_extract(str_extract(flight, "[:digit:]+ seconds,"), "[:digit:]+")
  r <- str_extract(str_extract(flight, "[:digit:]+ seconds\\."), "[:digit:]+")
  
  list(reindeer = d, speed = as.numeric(s), flighttime = as.numeric(f), resttime = as.numeric(r))
}

distanceTraveled <- function(speed, flighttime, resttime, secondstotal) {
  distance <- 0
  while(secondstotal > 0) {
    if(secondstotal > flighttime) {
      distance <- distance + speed * flighttime
    } else {
      distance <- distance + speed * secondstotal
    }
    secondstotal <- secondstotal - flighttime - resttime
  }
  distance
}

flight_paths <- lapply(flights, parseFlight)
max(sapply(flight_paths, function(fp) {
  distanceTraveled(fp$speed, fp$flighttime, fp$resttime, input_seconds)
}))
# Answer is 2655

# Part 2
df <- plyr::ldply(flight_paths, function(fp) {
  dist = sapply(1:input_seconds, function(i) {
    distanceTraveled(fp$speed, fp$flighttime, fp$resttime, i)
  })
  data.frame(reindeer = fp$reindeer, kilometers = dist, seconds = 1:input_seconds)
})

df <- dcast(df, seconds ~ reindeer, value.var="kilometers")

inthelead <- unlist(apply(df, 1, function(row) names(row[max(row) == row])))
max(table(inthelead))
# Answer is 1059
