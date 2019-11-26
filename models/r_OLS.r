#!/usr/bin/env Rscript
#install.packages('tidyverse')
#install.packages('rjson')
require(tidyverse)
require(jsonlite)

setwd('/Users/apple/Documents/_for_deletion/fromPythonPH FB/Simple-Projects/models')

# 153, 6
# [1] "Ozone"   "Solar.R" "Wind"    "Temp"    "Month"   "Day" 
# Ozone and Solar.R columns have a number of NA's which must be imputed, given that their 
datasets::airquality %>% summary()

main_data = airquality

airquality %>% select(Day) %>% 


boot = modelr::bootstrap(main_data, 100)
models = map(boot$strap, ~ lm(Ozone ~ ., data = ., na.rm = TRUE))
tidied = purrr::map_df(models, broom::tidy, .id = "id")

# plotting the 
tidied %>% filter(!(term == '(Intercept)')) %>%
  ggplot(aes(x = estimate)) + geom_histogram(fill = 'blue', color = 'white') + facet_wrap(~term) +
  theme(plot.title = element_text(color = 'red', size = 20),
        axis.title.x = element_text(color = 'blue', size= 15)) + 
  labs(title = "Bootstrapped OLS Estimates for mtcars data",
       y = 'Count', x= 'Parameter (Beta Estimate)',
       subtitle = 'The original data has been bootstrapped for 100 times.')

# setting the data
set.seed(1990)
split_pct = .7
sample_set = sample(seq_len(nrow(main_data)), size = floor(split_pct * nrow(main_data)))
train = main_data[sample_set,]
test = main_data[-sample_set,]

lm_model = lm(formula= mpg ~ . ,data = train)
lm_summ = summary(lm_model)

# we should set a threshold for the MAPE metric.
modelr::mape(lm_model, test)
modelr::rsquare(lm_model, train)

lm_model$fitted.values
stats::predict(lm_model, test)

# getting the residual plots
par(mfrow=c(2,2))
plot(lm_model)


# getting the histogram for the model residuals
# par(mfrow=c(1,1))
hist(lm_model$residuals, main = 'Histogram of Model Residuals',
     xlab = 'Standardized Residuals' ,ylab = 'Frequency')
curve(dnorm(x, mean = base::mean(lm_model$residuals), sd = stats::sd(lm_model$residuals)), 
      col = 2, lty = 2, lwd = 2, add = TRUE)

# We should denote the expected/normative behaviour for each plot
base = data_frame(lm_summ$coefficients)
       