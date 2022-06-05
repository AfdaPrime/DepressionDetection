# %%

import text_cleaning as tc
import test_h5 as model
# %%
str = ""

temp = ""

while(temp != "-1"):

    temp = input()

    if(temp != "-1"):
        str += temp

    str += "\n"
print(str)
# %%
x = tc.text_cleaning(str)

model.predict_sentiment([x])

# %%
