import streamlit as st
from Weather import check_weather
from Joke import jokes
from News import get_news
from Currency_Convertor import currency
from Github_profile import get_github_user

st.title("🌤️ Today's Weather")
city = st.text_input("Enter city name")

if st.button("Check Weather"):
    if city:
        weather = check_weather(city)

        if "error" in weather:
            st.error(weather['error'])
        else:
            st.success(f"Weather in {weather['city']}")
            st.write(f"🌡️ Temperature: {weather['temp']} °C")
            st.write(f"☁️ Condition: {weather['description']}")
    else:
        st.warning("Please enter a city")

st.header("😂 Joke of the day")
joke = jokes()
st.write("### Setup")
st.write(joke["setup"])

st.write("### Punchline")
st.success(joke["punchline"])

#st.header("📰 Top News")

#country = st.selectbox("Select a country",["us","in","gb","ca","au"])
# country = "us"
# news = get_news(country)

# if isinstance(news, dict) and "error" in news:
#     st.error(news["error"])

# else:
#     for i, article in enumerate(news["articles"], start=1):
#         st.subheader(f"News {i}")
#         st.write("**Title:**", article["title"])
#         st.write("**Author:**", article["author"])
#         st.write("**Description:**", article["description"])
#         st.write("**Source:**", article["source"]["name"])
#         st.write("🔗", article["url"])


# st.header("Currency Convertor")
# col1,col2,col3 = st.columns(3)

# with col1:
#     amount = st.number_input("Amount",width=50,min_value=1)
# with col2:
#     from_curr = st.text_input("Main curruncy Code",width=100,value="USD")
# with col3:
#     to_curr = st.text_input("Converting curruncy Code",width=100,value="INR")

# result,error = currency(amount,from_curr,to_curr)

# if from_curr:
#     if to_curr:
#         st.success(f"{amount}{from_curr.upper()} = {result} {to_curr.upper()}")
#     elif error:
#         st.error(error)

st.header("Github user info")
get_user = st.text_input("Enter the username: ")

details = get_github_user(get_user)

if get_user:
    st.write(details)
