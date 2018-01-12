library('tidyverse')
library(mapdata)
library(readr)
library(ggplot2)
Conflictdata <- read_csv("UCDPconflictdata.csv", 
                              col_types = cols(latitude = col_number(), 
                                               longitude = col_number()))
View(Conflictdata)

#The following process assigns the correct names to the number values in type_of_violence

conflict <- Conflictdata %>%
  mutate(
    violence = 'something'
      )

conflict$violence[conflict$type_of_violence == 1] <- 'State Violence'
conflict$violence[conflict$type_of_violence == 2] <- 'Non-State Violence'
conflict$violence[conflict$type_of_violence == 3] <- 'One-Sided Violence'

# This bar chart shows the relation between types of violence and the number of casualties, and color-codes the bars
# based on geographic region.

ggplot(data=conflict, aes(x=violence, y=best, fill= region)) +
  geom_bar(stat="identity")

# This chart shows the geographic distribution of conflicts, where the size of the dots is determined by the number of
# casualties involved. The color of the dots indicates whether it was an instance of state violence, non-state violence
# or one-sided violence.

ggplot(data = conflict) +
  geom_polygon(data = map_data('world'), mapping = aes(x=long, y=lat, group=group)) +
  geom_point(mapping = aes(y = latitude, x = longitude, colour = violence, size = best))


# This code is used to create a table with summary statistic (sum total and averages) for each type of violence.

conflict.deaths.stats <- conflict %>%
  group_by(violence) %>%
  summarize(sum(best), mean(best))

names(conflict.deaths.stats) <- c('violence', 'total', 'average')
