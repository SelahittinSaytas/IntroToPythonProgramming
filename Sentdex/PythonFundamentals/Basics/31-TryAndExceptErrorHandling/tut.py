import csv

with open("example.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)

    try:
        whatColor = input("What color do you wish to know the date of? ")
        if whatColor in colors:
            colorIndex = colors.index(whatColor.lower())
            theDate = dates[colorIndex]
            print("The date of",whatColor,"is",theDate)
        else:
            print("Color is not found or is not o color!")

    #except Exception, e
    except NameError as e:
        print(e)
    '''
    except Exception as e:
        print(e)
    '''
    print("Continuing...")

'''
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1])
'''
