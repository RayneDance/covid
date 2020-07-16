from datareader import covidReader
import pandas
import matplotlib
import matplotlib.pyplot as plt

reader = covidReader('us-states.csv')

reader.readFileContents()

#state = reader.getStateSet('Florida')
#state = reader.getAllDeaths()
state = reader.getDailyNewDeathsByState('Arkansas')
#state = reader.getDailyNewDeathsAll()
#state = reader.getDailyDeathsExcludingEarly()
#state = reader.getDailyDeathsSpecfic()


df = pandas.DataFrame(state,columns=['date', 'deaths'])

output = df.plot(x = 'date', y = 'deaths', kind='line')
plt.show()