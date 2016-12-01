library(digest)

inputs <- paste0("ckczppom", 1:10000000)

# Create MD5 hashes. Must set serialze to FALSE. 
# From the docs
# Setting [serialze] to FALSE allows to compare the digest output of 
# given character strings to known control output.
md5_hashes <- sapply(inputs, digest, algo="md5", serialize=FALSE)

# Part 1, five leading zeros
x00000 <- grepl("^00000", md5_hashes)
md5_hashes[x00000 == T][1]

# Part 2, six leading zeros
x000000 <- grepl("^0000000", md5_hashes)
md5_hashes[x000000 == T][1]