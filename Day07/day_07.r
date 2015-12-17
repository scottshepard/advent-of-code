library(stringr)

CIRCUITS <- readLines("data.txt")

findValue <- function(circuit_code, circuits = CIRCUITS) {
  # TODO complete this function
  assignment_circuit <- findAssignmentCircuit(circuit_code, circuits)
  dependencies <- findDependentCircuits(assignment_circuit)
  if(is.null(dependencies)) {
    print(paste("Evaluating", circuit_code))
    evaluateValue(assignment_circuit)
  } else {
    dependent_vals <- sapply(dependencies, findValue, circuits)
    assignment_circuit_new <- str_replace_all(assignment_circuit, dependent_vals)
    circuits <- str_replace(circuits, assignment_circuit, assignment_circuit_new)
    findValue(circuit_code, circuits)
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
  ans <- if(is.na(operator)) {
    as.numeric(str_extract(ac, "^([:digit:])+"))
  } else if(operator == "NOT") {
    bitwNot(as.numeric(str_extract(ac, "(?<=NOT )[:digit:]+")))
  } else if(operator == "AND") {
    
  } else if(operator == "OR") {
    
  } else if(operator == "LSHIFT") {
    
  } else if(operator == "RSHIFT") {
    a <- as.numeric(str_extract(ac, "^([:digit:])+"))
    n <- as.numeric(str_extract(ac, "(?<=RSHIFT )[:digit:]+"))
    bitwShiftR(a, n)
  }
  # NOT
    # only one value
  # AND 
    # always two values
  # OR
    # always two values
  # LSHIFT
    # only one value & shift num
  # RSHIFT
    # only one value & shift num
  ans
}