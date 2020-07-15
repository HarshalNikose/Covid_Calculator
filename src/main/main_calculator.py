from covid import Covid
covid = Covid()

print(covid.get_total_active_cases())
print(covid.get_total_deaths())
print(covid.get_total_confirmed_cases())
print(covid.get_total_recovered())

#-------------------------------------------------------------------------------------
#EDA
print(covid.get_status_by_country_name('india'))
covid.get_data()

countries = covid.list_countries()
print(countries)

#----------------------------------------Print Country List---------------------------------------
countryList = []
for k in countries:
    countryList.append(k["name"])

len(countryList)

#------------------------------------------Calculator-----------------------------------
countryData = []
for item in countryList:
    countryData = covid.get_status_by_country_name(item)
    try:
        if (countryData["active"] + countryData["deaths"] + countryData["recovered"]) == (countryData["confirmed"]):
            continue
        else:
            print(countryData)
    except:
        print("\n")
        print("I want to further make changes")
        print("ERROR FOR : \n", countryData)