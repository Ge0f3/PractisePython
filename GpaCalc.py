def calculateGPA():
	points = {'A+':4.0,'A':4.0,'A-':3.67,'B+':3.33,'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,'C-':1.67,'D+':1.33,'D':1.0,'F':0.0}
	print("welcome to GPA calculater \nEnter all your Grades line one bye one \nOnce your done Enter blank to exit")
	num_course = 0 
	total_points = 0
	done = False 
	while not done:
		grade= input("Grade: ")
		if grade == "":
			done=True
		elif grade not in points:
			print("Unknow grade '{0}' ,'{0}' is being ignored.".format(grade))
		else:
			total_points += points[grade]
			num_course += 1
	if(num_course>0):
		print("your CGPA is {}".format(total_points/num_course))
def checkGrade():
	print("welcome to Check your grade \nType in your grade and know your grade points.\nOnce your done Enter blank to exit.")
	points = {'A+':4.0,'A':3.8,'A-':3.67,'B+':3.33,'B':3.0,'B-':2.67,'C+':2.33,'C':2.0,'C-':1.67,'D+':1.33,'D':1.0,'F':0.0}
	done=False
	while not done:
		point = float(input("Grade: "))
		if point == "":
			done=True
		else:
			for grades,pointss in points.items():
				if(pointss==point):
					print("The Grade for the point {} is {}".format(point,grades))
def main():
	print("welcome \What do you want to do \n if Calculate CGPA Enter 1 or Enter 2 to checkGrade")
	option = int(input("option: "))
	if(option==1):
		calculateGPA()
	elif(option==2):
		checkGrade()
	else:
		print("Enter the correct option ")

if __name__ == '__main__':
	main()