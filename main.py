from postfix import postfix as pf
import csv

#Test Driver for Postfix Calculator Lab by Zion Choi

if __name__ == '__main__':
    tests = []

#opens a new reader and appends the sample tests into a list
    with open('tests.txt', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tests.append(row)

#runs each test in the list, writes it to the log.txt file and prints formatted solution
    calc = pf('')
    with open('log.txt', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter = ' ')
        for test in tests:
            calc.set_input(test[0])
            writer.writerow(calc.calculate())
            print('(' + test[0] + ') :  ' + str(calc.calculate()))