library("statcheck")
library(lubridate)
library(dplyr)
library(readr)
library(tidyverse)

# set working directory
# setwd("E:/UCSD/Lab/Computational Cognition Lab/GitHub/Fabricator")
# set working directory
setwd("/Users/loey/Desktop/Research/FakeNews/Fabricator")

# read csv file
paper <- read_csv('elsevier/cognition/extract_2010.csv')
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