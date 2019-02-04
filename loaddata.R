#!/usr/bin/env R

# load required packages
if (!require('lubridate')) { install.packages('lubridate') }
if (!require('stringr')) { install.packages('stringr') }

# declare URL to dfset
URL <- 'https://data.gov.au/dataset/7f90d314-fa64-4bae-8609-2e26ff48f6fa/resource/05390642-bdeb-4174-9bd5-c1df6e6d1e9e/download/2018-australian-sdg-indicator-9-2-2v2.csv'

# load df
df <- read.csv(URL)

dfNames<- colnames(df)
names(df) <- str_to_lower(dfNames)

summary(df)
show(df)

# working with the dataframe

df$date <- years(df$date)
df$manufacturing <- as.numeric(df$manufacturing)
df$total <- as.numeric(df$total)
df$proportion <- as.numeric(df$proportion)

# plot data

png(filename = 'manufacturing.png', width = 640, height = 480, units = 'px')
plot(x = as.Date.character(df$date, format = '%Y'),
     y = df$proportion,
     col = 'purple',
     xlab = 'Year', ylab = 'Proportion',
     main = 'Proportion of Manufacturing Employment by Year')
dev.off()

