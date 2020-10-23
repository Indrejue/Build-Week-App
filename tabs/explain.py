from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Explain

Initially I went into this with no preconcieved expectation.  I just tried to figure out what information was most likely to help the pet reach a home. So initially I took the data and cleaned it up.  it had a column called outcometype and and outcomesubtype.  Colors were all over the place as was the name and breed columns. With colors breed and name i made all the letters lower case to reduce some of the uniformity differences.  I then took all the colors split all the words up to be indiviual list pieces in the column and resorted them by alphabetical order. This was just incase there were duplicates that were a result of the colors being fliped in order.  I then converted any colors or breeds that had a value count of less then 20 to an other and any names witha less then 30 value count to other as well to further reduce the extreamly high cardinality I was facing from those columns. I had determined i wanted to take the outcome type column as my results but not in its original format.  I then noticed that the outcome subtype column was going to be leaky and take the data from the outcome type so i decided to have it be droped. I also took the date time column and split it based on year and month as 2 new columns and droped th original datetime column. Sex upon outcome had multiple pices of information I felt deserved their own columns so I used a lambda function to creat a fixed column based on if the sex upon outcom column listed the pet as intact spayed or nutered.  I also created anouther function based on if the column contained the word male or female to seperate the genders. Age upon outcome was also very messyand needed to be reformated into a way that could be used functionaly.  So I split the numbers from the indicator of month/year/week.  Then I used a formula to convert all the ages to a age by month column. With my data wrangled I now had a clearer picture of what is going on.  I then converted my Outcometype column into a 1 or 0 based on if the pet was addopted or returned to owner as 1 and everything else 0 because I wanted to determin if they would make it to a home.

I then placed my data through various models namely a logistic regressor, a random forest classifier, and a gradient booster and also tuned the random forest clasifier and gradient booster. My initial baseline acuracy which as this is a true false statment of do they go to a home or not was about 57.87%' saying they would go to a home.  My logistic regressor wound up with a score of 80.28%'.  My randome forest was 79.78%' before tuning and 81.64%' after tuning. Finaly my gradient boosting clasifier was 81.16%' before tuning and 81.39%' after tuning.  With random forest being the highes scoring model I decided that I might use that as my main model.  Before that though I had to check some other things.

So I decided I wanted to see what effect Age had on the data so i ploted out the PDP of age as displayed below. As we can see from the figure yes the age does affect within the first year but after that it trails off.

"""),
html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/AgePDP.png', style={'width':'100%'}),

(""" 
I then took my random forest model as it was my best performing model and graphed out the feature importances to see what was the most impotant features.
"""),

html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/FeaturesRF.png', style={'width':'100%'}),

(""" 
Then for comparison sake  I took my second best performing model the gradient booster and graphed out the feature importances to see what was the most impotant features.
"""),

html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/FeaturesGBC.png', style={'width':'100%'}),

("""
With this information I was able to conclude that the most important thing for a pet finding a home or not was wether it was fixed or not.  Now I just needed to pick a model and as a final check as I already had all the accuracy scores for the models was to see the change in the accuracy so I graphed all the ROC curves for each of my models. As you can see below the logistic regressor is in red the random forest model before tuning is in yellow the tunned random forest is in blue the gradient model before tuning is in green and after tunning is in pink. From these graphs we can see that the tunned random forest and both gradient boosting models were almost identical.  Thus as the random forest tuned was my best performing model even if by a small margin I decided to use that model.
"""),

html.Img(src='https://raw.githubusercontent.com/Indrejue/Build-Week-App/master/model/ROCcurve.png', style={'width':'100%'}),


]