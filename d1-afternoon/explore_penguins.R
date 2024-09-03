library(tidyverse)
library(palmerpenguins)
library(ggthemes)

# show all the columns
glimpse(penguins)

# Extract the island column
penguins[ , "island" ]

# Extract multiple columns
penguins[ , c("species","island")]

# Extract the second observation
penguins[ 2 , c("species","island")]

# you can use numbers to refer to columns
penguins[2,2]

# Create plot
ggplot(data = penguins, 
       mapping = aes(x = flipper_length_mm,
                                      y = body_mass_g, 
                                      color = species,
                                      shape = species)) +
  geom_point() + 
  scale_color_colorblind() + 
  geom_smooth(method = "lm")


# Create plot
ggplot(data = penguins) +
  geom_point(mapping = aes(x = flipper_length_mm,
                           y = body_mass_g, 
                           color = species,
                           shape = species)) + 
  geom_smooth(mapping = aes(x = flipper_length_mm,
                            y = body_mass_g), method = "lm") +
  scale_color_colorblind() + 
  xlab("Flipper length (mm)") +
  ylab("Body mass (g)") + 
  ggtitle("Relationship between body mass\nand flipper length")

ggsave(filename = "penguin-plot.pdf")

# plot distribution of bill length for all data
ggplot(data = penguins, mapping = aes(x = bill_length_mm)) +
  geom_histogram()

# plot distribution of bill length for males 
male_penguins <- penguins %>% filter(sex == "male")
ggplot(data = male_penguins, mapping = aes(x = bill_length_mm)) +
  geom_histogram()

# plot distribution of bill length for males and females comparing between species
ggplot(data = penguins %>% filter(!is.na(sex)),
       mapping = aes(x = bill_length_mm, fill = sex)) +
  scale_fill_colorblind() + 
  geom_histogram(position = "identity", alpha = 0.5) + 
  facet_grid(sex ~ species)

# Boxplot comparing body mass across different years by sex and species
ggplot(data = penguins, mapping = aes(x = factor(year), y = body_mass_g, fill = sex)) + 
  geom_boxplot() + 
  facet_grid(island ~ species)


