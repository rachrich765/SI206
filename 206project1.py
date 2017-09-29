import os
import filecmp
import csv
import sys
from operator import itemgetter
from datetime import date, datetime

def getData(file):
	reader = csv.DictReader(open(file))
	dict_list = []
	for line in reader:
		dict_list.append(line)
	return (dict_list)

#Sort based on key/column
def mySort(data,col):
	if col == 'First':
		sort_by_fname = sorted(data, key=itemgetter('First'))
		return sort_by_fname[0]['First'] + ' ' + sort_by_fname[0]['Last']
	if col == 'Last':
		sort_by_lname = sorted(data, key=itemgetter('Last'))
		return sort_by_lname[0]['First'] + ' ' + sort_by_lname[0]['Last']
	if col == 'Email':
		sort_by_email = sorted(data, key=itemgetter('Email'))
		return sort_by_email[0]['First'] + ' ' + sort_by_email[0]['Last']

#Create a histogram
def classSizes(data):
	class_counts = {}
	for stuff in data:
		classx = stuff.get('Class')
		try:
			class_counts[classx] += 1
		except :
				class_counts[classx] = 1
	sorted_classes = sorted(class_counts.items(), key = lambda x:x[1], reverse = True)
	return sorted_classes
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:

# Find the most common day of the year to be born
def findDay(a):
	list_of_days = []
	split_up_dates_list = []
	counter_of_days = {}
	for stuff in a:
		date_of_birth = stuff.get('DOB')
		broken_up_dates = date_of_birth.split('/')
		split_up_dates_list.append(broken_up_dates)
	for y in split_up_dates_list:
		list_of_days.append(y[1])
	for day in list_of_days:
		counter_of_days[day] = counter_of_days.get(day, 0) + 1
	sorted_dict_of_days = sorted(counter_of_days.items(), key = lambda x:x[1], reverse = True)
	return int(sorted_dict_of_days[0][0])

# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

# Find the average age (rounded) of the Students
def findAge(a):
	list_of_birthdays = []
	list_of_ages = []
	today = date.today()
	for stuff in a:
		date_of_birth = stuff.get('DOB')
		birthDate = datetime.strptime(date_of_birth, "%m/%d/%Y")
		list_of_birthdays.append(birthDate)
	for x in list_of_birthdays:
		age = today.year - x.year - ((today.month, today.day) < (x.month, x.day))
		list_of_ages.append(age)
	sum_of_ages = sum(list_of_ages)
	number_of_ages = len(list_of_ages)
	average_age = round(sum_of_ages / number_of_ages)
	return average_age

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	sorted_students = sorted(a, key = lambda x: x[col])
	csv_sorted_students_file = open(fileName, "w")
	for student_info in range(len(sorted_students)):
		file_write_info = sorted_students[student_info]['First'] + ',' + sorted_students[student_info]['Last']  + ','+ sorted_students[student_info]['Email']  + '\n'
		csv_sorted_students_file.write(file_write_info)
	csv_sorted_students_file.close()

# github username: rachrich765
################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
