library("statcheck")
library(lubridate)
library(dplyr)

# set working directory
# setwd("E:/UCSD/Lab/Computational Cognition Lab/GitHub/Fabricator")
# set working directory
setwd("E:/UCSD/Lab/Computational Cognition Lab/GitHub/Fabricator/")

# read csv file
paper <- read.csv(file = 'elsevier/cognition/extract_2010.csv', encoding = "UTF-8", header=TRUE, sep=",")
nrow(paper)

v1 <- paper[[3]]
# result <- 0

for (row in 1:nrow(paper)) {
  txt <- v1[row]
  stat <- statcheck(txt)
}

txt <- v1[46]
statcheck(v1[46])
stat <- statcheck(v1[46])