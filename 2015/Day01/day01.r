txt <- readLines("data.txt")

txt_vec <- strsplit(txt, "")[[1]]

txt_vec[txt_vec == "("] <- "1"
txt_vec[txt_vec == ")"] <- "-1"

txt_vec <- as.numeric(txt_vec)

# Part 1
sum(txt_vec) 
# Answer to Part 1 is 232

# Part 2
which(cumsum(txt_vec) == -1)[1]
# Answer to Part 2 is 1783