library(stringr)

instructions <- readLines("data.txt")
LIGHTGRID1 <- matrix(rep(-1, 1e7), nrow=1000)
LIGHTGRID2 <- matrix(rep(0, 1e7), nrow=1000)

# Part 1
controlLights1 <- function(x0, y0, x1, y1, instr) {
  x0 <- x0 - 1; y0 <- y0 - 1
  x1 <- x1 - 1; y1 <- y1 - 1
  
  if(instr == "on") {
    LIGHTGRID1[x0:x1, y0:y1] <<- 1
  } else if(instr == "off") {
    LIGHTGRID1[x0:x1, y0:y1] <<- -1
  } else if(instr == "toggle") {
    LIGHTGRID1[x0:x1, y0:y1] <<- 
      - LIGHTGRID1[x0:x1, y0:y1]
  } else {
    NULL
  }
}

# Extract Coordinates
parseInstruction <- function(instruction_line) {
  on_off_toggle <- str_extract(instruction_line, "on|off|toggle")
  coords <- str_extract_all(instruction_line, "[[:digit:]]*,[[:digit:]]*")[[1]]
  coords <- strsplit(coords, ",")
  names(coords) <- c("x", "y")
  coords <- lapply(coords, as.numeric)
  coords$instruction <- on_off_toggle
  coords
}

for(instruction in instructions) {
  l <- parseInstruction(instruction)
  controlLights1(l$x[1], l$x[2], l$y[1], l$y[2], l$instruction)
}

sum(LIGHTGRID1 == 1)
# Anwer is 400410

# Part 2
controlLights2 <- function(x0, y0, x1, y1, instr) {
  x0 <- x0 - 1; y0 <- y0 - 1
  x1 <- x1 - 1; y1 <- y1 - 1
  
  if(instr == "on") {
    LIGHTGRID2[x0:x1, y0:y1] <<- LIGHTGRID2[x0:x1, y0:y1] + 1
  } else if(instr == "off") {
    LIGHTGRID2[x0:x1, y0:y1] <<- LIGHTGRID2[x0:x1, y0:y1] - 1
    LIGHTGRID2[LIGHTGRID2 < 0] <<- 0
  } else if(instr == "toggle") {
    LIGHTGRID2[x0:x1, y0:y1] <<- LIGHTGRID2[x0:x1, y0:y1] + 2
  }
}

for(instruction in instructions) {
  l <- parseInstruction(instruction)
  controlLights2(l$x[1], l$x[2], l$y[1], l$y[2], l$instruction)
}

sum(LIGHTGRID2)
# Anwer is 15343601
