library(tidyverse)
library(ggthemes)


# Question 1
df <- read_delim("/data/learn/qb24/GTEx/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt")

# Question 2
glimpse(df)

# Question 3
truseq.df <- df %>%
  filter(SMGEBTCHT == "TruSeq.v1")


# Question 4 
ggplot(data = truseq.df %>% group_by(SMTSD) %>% summarize(n()), mapping = aes(x = SMTSD, y = `n()`)) + 
  geom_col() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  xlab("Tissue samples") + 
  ylab("Count")

# Question 5
ggplot(data = truseq.df, mapping = aes(x = SMRIN)) +
  geom_histogram(binwidth = 0.1)

# Question 6
ggplot(data = truseq.df, mapping = aes(x = SMTSD, y = SMRIN)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  xlab("Tissue samples") + 
  ylab("RNA integrity score")

# Question 7
ggplot(data = truseq.df, mapping = aes(x = SMGNSDTC)) + 
  geom_histogram() + 
  facet_grid(SMTSD ~ .)
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  xlab("Tissue samples") + 
  ylab("Count")
  
# Question 8
ggplot(data = truseq.df %>% filter(SMTSD == "Spleen" | SMTSD == "Testis" | SMTSD == "Uterus" | SMTSD == "Stomach" | SMTSD == "Thyroid"), mapping = aes(x = SMTSISCH, y = SMRIN)) + 
    geom_point(size = 0.5, alpha = 0.5) +
    facet_grid(SMTSD ~ .) +
    geom_smooth(method = "lm")

# Question 9
ggplot(data = truseq.df %>% filter(SMTSD == "Spleen" | SMTSD == "Testis" | SMTSD == "Uterus" | SMTSD == "Stomach" | SMTSD == "Thyroid"), mapping = aes(x = SMTSISCH, y = SMRIN, color = SMATSSCR)) + 
  geom_point(size = 0.5, alpha = 0.5) +
  facet_grid(SMTSD ~ .) +
  geom_smooth(method = "lm")

