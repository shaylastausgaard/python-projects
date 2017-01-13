#Shayla Stausgaard

class Country:
    def __init__(self,name, population, area, continent):
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent
    #generate a string representation for the class
    def __repr__(self):
        return (self._name +" "+ 'in' + " " + self._continent)

    def setPopulation(self, population):
        self._population = population

    def getName(self) :
        return self._name

    def getArea(self) :
        return self._area

    def getPopulation(self) :
        return self._population

    def getContinent(self):
        return self._continent

    # getPopDensity: the population divided by the area.
    def getPopDensity(self):
        return round((self._population / self._area),2)
    #successful test of all classes and methods completed before moving on to the next section

class CountryCatalogue:
    def __init__(self, file):
        #create empty dictonary
        self._catalogue = {}
        self._cDictonary = {}
        continents = open("continent.txt", 'r')
        continents.readline()
        #sort info and make Country the Key of the dictionary and Continent the value
        for line in continents:
            temp = line.split(',')
            temp[1] = temp[1].strip()
            self._cDictonary[temp[0]] = temp[1]
        continents.close()
        data = open(file, "r")
        data.readline()
        for line in data:
            relevantData = line.split("|")
            population = relevantData[1].replace(",", "")
            areaTemp = relevantData[2].replace(",", "")
            self._catalogue[relevantData[0]] = Country(relevantData[0] , int(population), float(areaTemp), self._cDictonary[relevantData[0]])
        data.close()


    def addCountry(self):
        #Give the user the option to add a new country to the set.
        print("If you would like to add a Country")
        country = input("Enter Country: ")
        for line in self._catalogue:
            if self._catalogue[line].getName().lower() == country.lower():
                country = input("Yay! This Country is already logged, you can now try another Country")
        population = input("Enter Population: ")
        area = input("Enter Area: ")
        continent = input("Enter Continent: ")
        self._catalogue[country] = [country, population, area, continent ]
        self._cDictonary[country] = continent
        print(country ,"was successfully logged.", "Population: ", population, "Area:", area, "Continent: ", continent)
        print("_"*200)


    def deleteCountry(self) :
        print("If you would like to delete a Country, be sure to capitalize when you enter ")
        country = (input("Enter a Country: "))
        if country in self._catalogue:
            del self._catalogue[country]
            print(country, "was deleted.")
        else :
            print("That country wasn't found.")
            print()
        print("_"*200)


    def findCountry(self):
         #allow the user to enter a specific countryName
        country = str(input("Enter the Country you would like to find: ")).lower()
        for line in self._catalogue:
            #if this country exists then print all of the country’s information
            if self._catalogue[line].getName().lower() == country.lower(): #list has no attribute getName
                countryObject = self._catalogue[line]
                print(countryObject.getName(), countryObject.getPopulation(), countryObject.getArea(), countryObject.getPopDensity())
                return
        print("Country not found.")
        print("_"*200)


    def filterCountriesByContinent(self):
        #allow the user to enter a specific continent (assume valid continent)
        continent = input("Please enter the continent you would like to enquire about: ")
        countriesInCont = []
        for line in self._catalogue:
            if self._catalogue[line].getContinent().lower() == continent.lower():
                countriesInCont.append(line)
        print(countriesInCont)
        print("_"*200)


    def printCountryCatalogue(self):
        for line in self._catalogue:
            print(line)
        print("_"*200)


    def setPopulationOfASelectedCountry(self):
        #Ask the user for a country name and new population
        print("Complete the following to set the population of a Country.")
        country = input("Enter Country: ")
        population = float(input("Enter Population: "))
        for line in self._catalogue:
            if self._catalogue[line].getName().lower() == country.lower():
                # and then set the population of the country (if it is in the catalogue) to the value
                self._catalogue[line].setPopulation(population)
                print(self._catalogue[line].getPopulation())
                #Print the new population density for that country to the screen.
                print("New population density for", country, ":", self._catalogue[line].getPopDensity())
                print("_"*200)
                return
        print("Country not found.")
        print("_"*200)


    #find and display the name of the country with the largest population to the screen
    def findCountryWithLargestPop(self):
        value = 0
        name = ""
        largestPopulation = 0
        for line in self._catalogue:
            if value == 0:
                largestPopulation = float(self._catalogue[line].getPopulation())
                name = self._catalogue[line].getName()
            if float(self._catalogue[line].getPopulation()) > largestPopulation:
                largestPopulation = float(self._catalogue[line].getPopulation())
                name = self._catalogue[line].getName()
            value = value + 1
        print(name, "has the largest population, with a population of: ", largestPopulation)
        print("_"*200)


    def findCountryWithSmallestArea(self):
        value = 0
        name = ""
        smallestArea = 0
        for line in self._catalogue:
            if value == 0:
                smallestArea = float(self._catalogue[line].getArea())
                name = self._catalogue[line].getName()
            if float(self._catalogue[line].getArea()) < smallestArea:
                smallestArea = float(self._catalogue[line].getArea())
                name = self._catalogue[line].getName()
            value = value + 1
        print(name, "is the Counrty with the smallest area, with an area of: ", smallestArea)
        print("_"*200)


    def findMostPopulousContinent(self):
        value = 0
        continent = ""
        mostPopulous = 0
        mostPopulousName = ""
        for line in self._catalogue:
            if self._catalogue[line].getPopulation() > mostPopulous:
                mostPopulous = self._catalogue[line].getPopulation()
                mostPopulousName = self._catalogue[line].getContinent()
        print("The Continent with the highest population is:",mostPopulousName, "with a population of" , mostPopulous)
        print("_"*200)

    def filterCountriesByPopDensity(self):
        #ask the user to enter the lower bound and upper bound for a population density range
        lower = input("Please enter the lowest population density you would like to search for: ")
        upper = input("Please enter the highest population density you would like to search for ")
        withinRange = []
        for line in self._catalogue:
            #find all countries that have a population density that falls within the range
            if float(lower) <= self._catalogue[line].getPopDensity() <= float(upper):
                withinRange.append(self._catalogue[line].getName())
        print("The Countries that are within your desired range are as follows:")
        print(withinRange)
        print("_"*200)

    def saveCountryCatalogue(self, filename):
        infoToBeSaved = []
        outputFile = open("output.txt", "w")
        # Sample provided: Name|Continent|Population|PopulationDensity
        outputFile.write("Name|Continent|Population|PopulationDensity")
        for line in self._catalogue:
            strToAppend = ""
            name = self._catalogue[line].getName()
            continent = self._catalogue[line].getContinent()
            population = str(self._catalogue[line].getPopulation())
            populationDensity = str(self._catalogue[line].getPopDensity())
            strToAppend = name + "|" + continent + "|" + population + "|" + populationDensity
            infoToBeSaved.append(strToAppend)
        #sort Countries alphabetically by name prior to saving.
        for line in sorted(infoToBeSaved):
            countriesSaved = ""
            for i in line:
                countriesSaved = countriesSaved +str(i)
            #allow the user to save all the countries to a file.
            outputFile.write(countriesSaved)
            print(countriesSaved)
        outputFile.close()
        print("All changes have been saved")
        print("_"*200)
