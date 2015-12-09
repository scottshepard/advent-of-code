txt <- readLines("data.txt")

txt_vec <- strsplit(txt, "")[[1]]

txt_vec[txt_vec == "("] <- "1"
txt_vec[txt_vec == ")"] <- "-1"

txt_vec <- as.numeric(txt_vec)

sum(txt_vec)