library("statcheck")
library(lubridate)
library(dplyr)

# set working directory
setwd("E:/UCSD/Lab/Computational Cognition Lab/GitHub/Fabricator")

"""files <- list.files(path="htmls/clean", pattern="*.html", full.names=TRUE, recursive=TRUE)
for (file in files){ # load file
# apply function
out <- checkHTML(file)
# write to file
write.table(out, file = "output.txt")
}"""


out <- checkdir("htmls/clean", subdir = FALSE)
write.table(out, file = "outputFile.txt")
write.csv(out, file = "outputFile.csv")


print(checkHTML("htmls/clean/BrownCronkGrochow_2005_DanceRevealsSymmetry.html"))

print(checkHTML("htmls/clean/One and Done_ Optimal Decisions From Very Few Samples - Vul - 2014 - Cognitive Science - Wiley Online Library.htm"))

print(checkHTML("htmls/clean/AndersonAwh_2012_ThePlateauInMnemonicResolution.html"))