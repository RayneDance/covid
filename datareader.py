import csv

class covidReader:

    def __init__(self, file):

        #contains data for all entries by date
        self.data = {}

        self.filehandle = self.openFile(file)


    def openFile(self, file):

        try:
            file = open(file, 'r', newline='')

            print("File opened: "+str(file))

            return file
        except OSError as err:
            print(err)
            return False

    def getStateSet(self, state):
        data = {'date':[], 'deaths':[]}

        for val in self.data:
            try:
                data['deaths'].append(int(self.data[val][state]))
                data['date'].append(val)
            except:
                continue
        print(data)
        return data

    def getDailyNewDeathsByState(self, state):

        data = {'date':[], 'deaths':[]}
        previous = 0
        for val in self.data:
            try:
                current = int(self.data[val][state])

                data['deaths'].append(current - previous)
                data['date'].append(val)
                previous = current
            except:
                continue
        print(data)
        return data

    def getDailyNewDeathsAll(self):

        data = {'date':[], 'deaths':[]}
        previous = 0
        for val in self.data:
            res = 0
            for state in self.data[val]:
                res += int(self.data[val][state])

            data['deaths'].append(res - previous)
            data['date'].append(val)
            previous = res
        return data

    def getDailyDeathsExcludingEarly(self):
        data = {'date':[], 'deaths':[]}
        skip = {'New York':True, 'New Jersey':True, 'Massachusetts':True, 'California':True, 'Washington':True, 'Chicago':True,
                'Connecticut':True, 'New Hampshire':True, 'Rhode Island':True, 'Delaware':True, 'Maine':True, 'Michigan':True}
        previous = 0
        for val in self.data:
            res = 0
            for state in self.data[val]:
                if state in skip:
                    continue
                res += int(self.data[val][state])

            data['deaths'].append(res - previous)
            data['date'].append(val)
            previous = res
        return data

    def getDailyDeathsSpecfic(self):
        data = {'date':[], 'deaths':[]}
        skip = {'Texas':True, 'Louisiana':True, 'Georgia':True, 'Florida':True,
                'Alabama':True, 'Mississippi':True, 'South Carolina':True, 'North Carolina':True,
                'Oklahoma':True, 'Arkansas':True, 'Tennessee':True}
        previous = 0
        for val in self.data:
            res = 0
            for state in self.data[val]:
                if state in skip:
                    continue
                res += int(self.data[val][state])

            data['deaths'].append(res - previous)
            data['date'].append(val)
            previous = res
        return data

    def getAllDeaths(self):
        data = {'date':[], 'deaths':[]}

        for val in self.data:
            res = 0
            for state in self.data[val]:
                if self.data[val][state] == 'deaths':
                    continue
                res += int(self.data[val][state])

            data['deaths'].append(res)
            data['date'].append(val)
        return data
    
    def readFileContents(self):

        if self.filehandle:
            content  = csv.reader(self.filehandle, delimiter=',', quotechar='|')
            for row in content:
                if row[0] == 'date':
                    continue
                
                if row[4] == '0':
                    continue

                if row[0] in self.data:
                    self.data[row[0]].update({row[1]:row[4]})
                else:

                    self.data.update({row[0]:{row[1]:row[4]}})

        #print(self.data['2020-07-14']['Texas'])