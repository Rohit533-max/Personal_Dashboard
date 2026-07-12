from Currency_Convertor import currency
from Github_profile import get_github_user
from Joke import jokes
from News import get_news
from Weather import check_weather


print('='*100)
print("                                    Today's Dashboard                                    ")
print('='*100)
check_weather("chandigarh")

print('='*100)
currency()
print('='*100)
get_news()
print('='*100)
get_github_user("cz")
print('='*100)
jokes()
print('='*100)
