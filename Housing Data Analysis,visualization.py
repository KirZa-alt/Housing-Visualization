import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv(r"C:\Users\acer\Documents\kiran-python\hosuing visualization\housing.csv")


st.title("Housing Data:")
st.write(data)



# Histogram
fig, ax = plt.subplots()
data["area"].plot(kind="hist", bins=20, edgecolor="black", ax=ax)
ax.set_title("Distribution of House Area")
ax.set_xlabel("Area")
st.pyplot(fig)

st.markdown("""
### 1️⃣ Distribution of House Area
When we plot the distribution of house area, we notice most houses fall into a smaller size range, but there are some giant houses far above the rest.  
These outliers — like the ones with areas in the tens of thousands of square feet — stretch the graph to the right, giving it a positively skewed shape.

This means while most homes are modest in size, a handful are unusually large.
""")


# 2️⃣ Area vs Price Relationship
fig1, ax1 = plt.subplots()
data.plot(kind="scatter", x="area", y="price", alpha=0.5, ax=ax1)
ax1.set_title("Area vs Price")
st.pyplot(fig1)

st.markdown("""
### 2️⃣ Area vs Price Relationship
Our scatter plot of area vs price tells a clear story:  
As area increases, price generally increases too — a direct relationship.  

But the points aren’t perfectly aligned:  
- Some large houses aren’t as expensive as you’d expect.  
- Some smaller houses are surprisingly costly.  

This hints that location, furnishing, and other features also influence price beyond just size.
""")

# 3️⃣ Price by Bedrooms
fig2, ax2 = plt.subplots()
data.boxplot(column="price", by="bedrooms", ax=ax2)
ax2.set_title("Price by Bedrooms")
plt.suptitle("")  # Remove default subtitle
ax2.set_ylabel("Price")
st.pyplot(fig2)

st.markdown("""
### 3️⃣ Price by Number of Bedrooms
The box plot comparing price by bedrooms reveals that:  
1. Homes with more bedrooms generally have higher prices.  
2. There’s still a wide range of prices for the same bedroom count, again pointing to other factors influencing value.  
3. Outliers in price exist here too — some houses with fewer bedrooms are more expensive than those with more rooms, likely due to premium locations or luxury furnishing.
""")


# 4️⃣ Furnishing Status and Price
st.subheader("4️⃣ Furnishing Status and Price")

fig4, ax4 = plt.subplots()
data.groupby("furnishingstatus")["price"].mean().plot(kind="bar", ax=ax4)
ax4.set_title("Average Price by Furnishing Status")
ax4.set_ylabel("Price")
st.pyplot(fig4)

st.write("""
1. Furnished houses command the highest prices.  
2. Semi-furnished homes sit in the middle range.  
3. Unfurnished properties tend to be the cheapest on average.  
4. This suggests that buyers are willing to pay more for the convenience and appeal of a ready-to-move-in property.
""")

# 🏡 Overall Story
st.subheader("🏡 Overall Story")
st.write("""
The Housing dataset paints a vivid picture of a diverse real estate market.  

- Bigger houses generally cost more, but outliers in both area and price show that some properties defy expectations.  
- Furnished homes tend to command premium prices.  
- More bedrooms often push prices higher, but location and amenities can make a smaller home just as valuable as a larger one.  

💡 The data tells us one thing clearly:  
In real estate, numbers matter — but the real story lies in the unique combination of size, features, and desirability.
""")


