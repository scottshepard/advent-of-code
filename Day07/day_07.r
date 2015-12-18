library(stringr)

CIRCUITS <- readLines("data.txt")
KNOWNVALUES = data.frame()

findValue <- function(circuit_code, circuits = CIRCUITS) {
  # Recursive function to find the value of a given circuit code
  
  # First check to see if that value has been evaluated before and 
  # return if it has. This will prevent reevaluating the same code 
  # and thus prevent long runtimes
  if(circuit_code %in% KNOWNVALUES$code) {
    return(KNOWNVALUES[KNOWNVALUES$code == circuit_code, ]$value)
  } else {
    assignment_circuit <- findAssignmentCircuit(circuit_code, circuits)
    dependencies <- findDependentCircuits(assignment_circuit)
    if(is.null(dependencies)) {
      print(paste("Evaluating", circuit_code))
      ans <- evaluateValue(assignment_circuit)
      KNOWNVALUES <<- rbind(KNOWNVALUES, data.frame(code = circuit_code, value = ans))
      ans
    } else {
      dependent_vals <- sapply(dependencies, findValue, circuits)
      assignment_circuit_new <- str_replace_all(assignment_circuit, dependent_vals)
      circuits <- str_replace(circuits, assignment_circuit, assignment_circuit_new)
      findValue(circuit_code, circuits)
    }
  }
}

findAssignmentCircuit <- function(code, circuits = CIRCUITS) {
  circuits[grepl(paste0("-> ", code, "$"), circuits)]
}

findDependentCircuits <- function(circuit, circuits = CIRCUITS) {
  output <- setdiff(
    str_extract_all(circuit, "\\b[a-z]{1,2}\\b")[[1]], 
    str_extract(circuit, "[a-z]+$")
  )
  if(length(output) == 0) {
    NULL
  } else {
    output
  }
}

evaluateValue <- function(ac) {
### Cases
  valcode <- str_extract(ac, "[a-z]+$")
  operator <- str_extract(ac, "[A-Z]+")
  if(is.na(operator)) {
    as.numeric(str_extract(ac, "^(-?[:digit:])+"))
  } else if(operator == "NOT") {
    bitwNot(as.numeric(str_extract(ac, "(?<=NOT )-?[:digit:]+")))
  } else if(operator == "AND") {
    a <- as.numeric(str_extract(ac, "-?[:digit:]+(?= AND)"))
    b <- as.numeric(str_extract(ac, "(?<=AND )-?[:digit:]+"))
    bitwAnd(a, b)
  } else if(operator == "OR") {
    a <- as.numeric(str_extract(ac, "-?[:digit:]+(?= OR)"))
    b <- as.numeric(str_extract(ac, "(?<=OR )-?[:digit:]+"))
    bitwOr(a, b)
  } else if(operator == "LSHIFT") {
    a <- as.numeric(str_extract(ac, "^(-?[:digit:])+"))
    n <- as.numeric(str_extract(ac, "(?<=LSHIFT )-?[:digit:]+"))
    bitwShiftL(a, n)
  } else if(operator == "RSHIFT") {
    a <- as.numeric(str_extract(ac, "^(-?[:digit:])+"))
    n <- as.numeric(str_extract(ac, "(?<=RSHIFT )-?[:digit:]+"))
    bitwShiftR(a, n)
  }
}

# Part 1
findValue("a")
# Answer is 3176

# Part 2
# Change data.txt so that 3176 -> b 
# Then rerun
findValue("a")
