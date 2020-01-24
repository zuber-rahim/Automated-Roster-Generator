import random 
from random import randint

class Employee(object):
    """ Stores details on an operator. """

    def __init__(self):
        self.id = None
        self.first_name = None
        self.family_name = None
        self.contracted_hours = None
        self.hours_done = None
        self.dayOff_1 = None
        self.dayOff_2 = None
        self.dayOff_3 = None
        self.dayOff_4 = None
        self.dayOff_5 = None
        self.dayOff_6 = None
        self.leave1 = None
        self.leave2 = None
        self.leave3 = None
        self.leave4 = None
        self.leave5 = None
        self.leave6 = None
        self.leave7 = None
        
    def create_emp(self, num, day, month):
        employees = []
        op = Employee()
        op.id = "?"
        op.XP = 10
        op.first_name = "Salman"
        op.family_name = "Malik"
        op.contracted_hours = 45
        op.hours_done = 0
        op.dayOff_1 = "Friday"
        op.dayOff_2 = "Saturday"
        op.dayOff_3 = "-"
        op.dayOff_4 = "-"
        op.dayOff_5= "-"
        op.dayOff_6= "-"
        op.leave1 = '-'
        op.leave2 = '-'
        op.leave3 = '-'
        op.leave4 = '-'
        op.leave5 = '-'
        op.leave6 = '-'
        op.leave7 = '-'
        employees.append(op)
        
        op1 = Employee()
        op1.id = "t826360"
        op1.XP = 7
        op1.first_name = "Zuber"
        op1.family_name = "Rahim"
        op1.contracted_hours = 15
        op1.hours_done = 0
        op1.dayOff_1 = "Saturday"
        op1.dayOff_2 = "Tuesday"
        op1.dayOff_3 = "Wednesday"
        op1.dayOff_4 = "Thursday"
        op1.dayOff_5= "Friday"
        op1.dayOff_6= "-"
        op1.leave1 = '-'
        op1.leave2 = '-'
        op1.leave3 = '-'
        op1.leave4 = '-'
        op1.leave5 = '-'
        op1.leave6 = '-'
        op1.leave7 = '-'
        employees.append(op1)
        
        op2 = Employee()
        op2.id = "?"
        op2.XP = 10
        op2.first_name = "Leon"
        op2.family_name = "Crichton"
        op2.contracted_hours = 45
        op2.hours_done = 0
        op2.dayOff_1 = "Tuesday"
        op2.dayOff_2 = "Thursday"
        op2.dayOff_3 = "-"
        op2.dayOff_4 = "-"
        op2.dayOff_5= "-"
        op2.dayOff_6= "-"
        op2.leave1 = '-'
        op2.leave2 = '-'
        op2.leave3 = '-'
        op2.leave4 = '-'
        op2.leave5 = '-'
        op2.leave6 = '-'
        op2.leave7 = '-'
        employees.append(op2)
        
        op3 = Employee()
        op3.id = "?"
        op3.XP = 10
        op3.first_name = "Nick"
        op3.family_name = "Diamzon"
        op3.contracted_hours = 40
        op3.hours_done = 0
        op3.dayOff_1 = "Sunday"
        op3.dayOff_2 = "Monday"
        op3.dayOff_3 = "-"
        op3.dayOff_4 = "-"
        op3.dayOff_5= "-"
        op3.dayOff_6= "-"
        op3.leave1 = '-'
        op3.leave2 = '-'
        op3.leave3 = '-'
        op3.leave4 = '-'
        op3.leave5 = '-'
        op3.leave6 = '-'
        op3.leave7 = '-'
        employees.append(op3)
        
        op4 = Employee()
        op4.id = "?"
        op4.XP = 6
        op4.first_name = "Jemima"
        op4.family_name = "Mendoro"
        op4.contracted_hours = 30
        op4.hours_done = 0
        op4.dayOff_1 = "Sunday"
        op4.dayOff_2 = "Saturday"
        op4.dayOff_3 = "-"
        op4.dayOff_4 = "-"
        op4.dayOff_5= "-"
        op4.dayOff_6= "-"
        op4.leave1 = '-'
        op4.leave2 = '-'
        op4.leave3 = '-'
        op4.leave4 = '-'
        op4.leave5 = '-'
        op4.leave6 = '-'
        op4.leave7 = '-'
        employees.append(op4)
        
        op5 = Employee()
        op5.id = "?"
        op5.XP = 7
        op5.first_name = "Daniel"
        op5.family_name = "Seng"
        op5.contracted_hours = 15
        op5.hours_done = 0
        op5.dayOff_1 = "Monday"
        op5.dayOff_2 = "Tuesday"
        op5.dayOff_3 = "Wednesday"
        op5.dayOff_4 = "Thursday"
        op5.dayOff_5= "Friday"
        op5.dayOff_6= "-"
        op5.leave1 = '-'
        op5.leave2 = '-'
        op5.leave3 = '-'
        op5.leave4 = '-'
        op5.leave5 = '-'
        op5.leave6 = '-'
        op5.leave7 = '-'
        employees.append(op5)
        
        op6 = Employee()
        op6.id = "?"
        op6.XP = 9
        op6.first_name = "Ace"
        op6.family_name = "Osit"
        op6.contracted_hours = 20
        op6.hours_done = 0
        op6.dayOff_1 = "Monday"
        op6.dayOff_2 = "Tuesday"
        op6.dayOff_3 = "Wednesday"
        op6.dayOff_4 = "Thursday"
        op6.dayOff_5= "Friday"
        op6.dayOff_6= "-"
        op6.leave1 = '-'
        op6.leave2 = '-'
        op6.leave3 = '-'
        op6.leave4 = '-'
        op6.leave5 = '-'
        op6.leave6 = '-'
        op6.leave7 = '-'
        employees.append(op6)
        
        op7 = Employee()
        op7.id = "?"
        op7.XP = 8
        op7.first_name = "Devyani"
        op7.family_name = "Patel"
        op7.contracted_hours = 40
        op7.hours_done = 0
        op7.dayOff_1 = "Friday"
        op7.dayOff_2 = "Saturday"
        op7.dayOff_3 = "-"
        op7.dayOff_4 = "-"
        op7.dayOff_5= "-"
        op7.dayOff_6= "-"
        op7.leave1 = '-'
        op7.leave2 = '-'
        op7.leave3 = '-'
        op7.leave4 = '-'
        op7.leave5 = '-'
        op7.leave6 = '-'
        op7.leave7 = '-'
        employees.append(op7)
        
        op8 = Employee()
        op8.id = "?"
        op8.XP = 7
        op8.first_name = "Cameron"
        op8.family_name = "Laiolay"
        op8.contracted_hours = 15
        op8.hours_done = 0
        op8.dayOff_1 = "Monday"
        op8.dayOff_2 = "Tuesday"
        op8.dayOff_3 = "Wednesday"
        op8.dayOff_4 = "Thursday"
        op8.dayOff_5= "Sunday"
        op8.dayOff_6= "-"
        op8.leave1 = '-'
        op8.leave2 = '-'
        op8.leave3 = '-'
        op8.leave4 = '-'
        op8.leave5 = '-'
        op8.leave6 = '-'
        op8.leave7 = '-'
        employees.append(op8)
        
        op9 = Employee()
        op9.id = "?"
        op9.XP = 7
        op9.first_name = "Reema"
        op9.family_name = "Singh"
        op9.contracted_hours = 18
        op9.hours_done = 0
        op9.dayOff_1 = "Monday"
        op9.dayOff_2 = "Tuesday"
        op9.dayOff_3 = "Wednesday"
        op9.dayOff_4 = "Thursday"
        op9.dayOff_5= "Sunday"
        op9.dayOff_6= "-"
        op9.leave1 = '-'
        op9.leave2 = '-'
        op9.leave3 = '-'
        op9.leave4 = '-'
        op9.leave5 = '-'
        op9.leave6 = '-'
        op9.leave7 = '-'
        employees.append(op9)
        
        op10 = Employee()
        op10.id = "?"
        op10.XP = 7
        op10.first_name = "Russell"
        op10.family_name = "-"
        op10.contracted_hours = 9
        op10.hours_done = 0
        op10.dayOff_1 = "Monday"
        op10.dayOff_2 = "Tuesday"
        op10.dayOff_3 = "Wednesday"
        op10.dayOff_4 = "Thursday"
        op10.dayOff_5= "Friday"
        op10.dayOff_6= "Sunday"
        op10.leave1 = '-'
        op10.leave2 = '-'
        op10.leave3 = '-'
        op10.leave4 = '-'
        op10.leave5 = '-'
        op10.leave6 = '-'
        op10.leave7 = '-'
        employees.append(op10)
        
        op11 = Employee()
        op11.id = "?"
        op11.XP = 8
        op11.first_name = "Aashmi"
        op11.family_name = "Santosh"
        op11.contracted_hours = 28
        op11.hours_done = 0
        op11.dayOff_1 = "Tuesday"
        op11.dayOff_2 = "Wednesday"
        op11.dayOff_3 = "Saturday"
        op11.dayOff_4 = "Sunday"
        op11.dayOff_5= "-"
        op11.dayOff_6= "-"
        op11.leave1 = '-'
        op11.leave2 = '-'
        op11.leave3 = '-'
        op11.leave4 = '-'
        op11.leave5 = '-'
        op11.leave6 = '-'
        op11.leave7 = '-'
        employees.append(op11)
        
        op12 = Employee()
        op12.id = "?"
        op12.XP = 8
        op12.first_name = "Jessica"
        op12.family_name = "-"
        op12.contracted_hours = 15
        op12.hours_done = 0
        op12.dayOff_1 = "Monday"
        op12.dayOff_2 = "Tuesday"
        op12.dayOff_3 = "Wednesday"
        op12.dayOff_4 = "Thursday"
        op12.dayOff_5= "Saturday"
        op12.dayOff_6= "-"
        op12.leave1 = '-'
        op12.leave2 = '-'
        op12.leave3 = '-'
        op12.leave4 = '-'
        op12.leave5 = '-'
        op12.leave6 = '-'
        op12.leave7 = '-'
        employees.append(op12)
        
        op13 = Employee()
        op13.id = "?"
        op13.XP = 10
        op13.first_name = "Suzzanne"
        op13.family_name = "Lee-Chan"
        op13.contracted_hours = 45
        op13.hours_done = 0
        op13.dayOff_1 = "Sunday"
        op13.dayOff_2 = "Monday"
        op13.dayOff_3 = "-"
        op13.dayOff_4 = "-"
        op13.dayOff_5= "-"
        op13.dayOff_6= "-"
        op13.leave1 = '-'
        op13.leave2 = '-'
        op13.leave3 = '-'
        op13.leave4 = '-'
        op13.leave5 = '-'
        op13.leave6 = '-'
        op13.leave7 = '-'
        employees.append(op13)
        
        op14 = Employee()
        op14.id = "?"
        op14.XP = 8
        op14.first_name = "Ornella"
        op14.family_name = "Matty"
        op14.contracted_hours = 15
        op14.hours_done = 0
        op14.dayOff_1 = "Tuesday"
        op14.dayOff_2 = "Wednesday"
        op14.dayOff_3 = "Thursday"
        op14.dayOff_4 = "Saturday"
        op14.dayOff_5= "Sunday"
        op14.dayOff_6= "-"
        op14.leave1 = '-'
        op14.leave2 = '-'
        op14.leave3 = '-'
        op14.leave4 = '-'
        op14.leave5 = '-'
        op14.leave6 = '-'
        op14.leave7 = '-'
        employees.append(op14)
        
        op15 = Employee()
        op15.id = "?"
        op15.XP = 10
        op15.first_name = "Naomi"
        op15.family_name = "-"
        op15.contracted_hours = 40
        op15.hours_done = 0
        op15.dayOff_1 = "Sunday"
        op15.dayOff_2 = "Monday"
        op15.dayOff_3 = "-"
        op15.dayOff_4 = "-"
        op15.dayOff_5= "-"
        op15.dayOff_6= "-"
        op15.leave1 = '-'
        op15.leave2 = '-'
        op15.leave3 = '-'
        op15.leave4 = '-'
        op15.leave5 = '-'
        op15.leave6 = '-'
        op15.leave7 = '-'
        employees.append(op15)
        
        op16 = Employee()
        op16.id = "?"
        op16.XP = 10
        op16.first_name = "Kelvin"
        op16.family_name = "-"
        op16.contracted_hours = 7
        op16.hours_done = 0
        op16.dayOff_1 = "Monday"
        op16.dayOff_2 = "Tuesday"
        op16.dayOff_3 = "Thursday"
        op16.dayOff_4 = "Friday"
        op16.dayOff_5= "Sunday"
        op16.dayOff_6= "-"
        op16.leave1 = '-'
        op16.leave2 = '-'
        op16.leave3 = '-'
        op16.leave4 = '-'
        op16.leave5 = '-'
        op16.leave6 = '-'
        op16.leave7 = '-'
        employees.append(op16)
        
        
        

        if day == 'Monday':
            count = 0
        if day == 'Tuesday':
            count = 1
        if day == 'Wednesday':
            count = 2
        if day == 'Thursday':
            count = 3
        if day == 'Friday':
            count = 4
        if day == 'Saturday':
            count = 5
        if day == 'Sunday':
            count = 6
        #for i in employees:
        #   print(i.first_name +' '+ i.family_name +' '+str(i.contracted_hours)+' '+str(i.hours_done)+' '+i.dayOff_1+' '+i.dayOff_2+' '+i.dayOff_3+' '+i.dayOff_4+' '+i.dayOff_5)
        week = 1
        for x in range(num):
            num_of_emps_opening = 0
            num_of_emps_closing = 0
            num_of_emps_latenight = 0
            print(" ")
            print('Day: '+ day+' '+str(x+1)+' '+month)
            print('----------------------------------------------------------------------')
            if count >= 6:
                count = 0
            else:
                count = count + 1
            for i in employees:
                if count == 6:
                    i.hours_done = 0
                #print(str(i.XP)+' '+i.first_name +' '+ i.family_name +' '+str(i.contracted_hours)+' '+str(i.hours_done)+' '+i.dayOff_1+' '+i.dayOff_2+' '+i.dayOff_3+' '+i.dayOff_4+' '+i.dayOff_5)
                
                if i.dayOff_1 == day or i.dayOff_2 == day or i.dayOff_3 == day or i.dayOff_4 == day or i.dayOff_5 == day or i.dayOff_6 == day:
                    print(i.first_name+" has the day off")
                elif i.leave1 == x+1:
                    print(i.first_name + ' is on leave')
                elif i.leave2 == x+1:
                    print(i.first_name + ' is on leave')
                elif i.leave3 == x+1: 
                    print(i.first_name + ' is on leave')
                elif i.leave4 == x+1:
                    print(i.first_name + ' is on leave')
                elif i.leave5 == x+1:
                    print(i.first_name + ' is on leave')
                elif i.leave6 == x+1:
                    print(i.first_name + ' is on leave')
                elif i.leave7 == x+1:
                    print(i.first_name + ' is on leave')
                else:
                    if i.hours_done < i.contracted_hours - 9:
                        #print("stop for "+ i.first_name) 
                        i.hours_done += 9
                        if day == 'Thursday' or day == 'Friday':
                            shift = randint(1,3)
                        else:
                            shift = randint(1,2)
                    elif i.hours_done != i.contracted_hours or i.hours_done < i.contracted_hours - 9:
                        time_to_add = i.contracted_hours - i.hours_done
                        print(i.first_name+' has '+str(time_to_add)+' this is the time remaining.')
                        i.hours_done += time_to_add
                        if day == 'Thursday' or day == 'Friday':
                            if time_to_add == 7:
                                shift = randint(4, )
                            
                        else:
                            shift = randint(1,2)
                    
                    if shift == 1:
                        print(i.first_name+' 8:30am - 6:00pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_opening += 1
                    elif shift == 2:
                        print(i.first_name+' 9:45am - 7:15pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_closing += 1
                    elif shift == 3:
                        print(i.first_name+' 11:45am - 9:15pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_latenight += 1
                    elif shift == 4:
                        print(i.first_name+' 12:45am - 9:15pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_latenight += 1
                    elif shift == 5:
                        print(i.first_name+' 9:00am - 3:30pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_latenight += 1
                    elif shift == 6:
                        print(i.first_name+' 12:45pm - 7:15pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_latenight += 1
                    elif shift == 7:
                        print(i.first_name+' 2:45pm - 9:15pm [Contracted Hours: '+ str(i.contracted_hours)+' | Hours Done: '+str(i.hours_done)+']')
                        num_of_emps_latenight += 1
                     
            print(' ')
            print('Number of employees opening: ' +str(num_of_emps_opening))
            print('Number of employees closing: ' +str(num_of_emps_closing))
            print('Number of employees doing late night closing: ' +str(num_of_emps_latenight))
            print('Total number of employees rostered: '+ str(num_of_emps_opening + num_of_emps_closing + num_of_emps_latenight))
            print('----------------------------------------------------------------------')
                       
            if count == 0:
                day = 'Monday'
            if count == 1:
                day = 'Tuesday'
            if count == 2:
                day = 'Wednesday' 
            if count == 3:
                day = 'Thursday'
            if count == 4:
                day = 'Friday'
            if count == 5:
                day = 'Saturday'
            if count == 6:
                day = 'Sunday'
                
            
if __name__ == '__main__': 
    app = Employee()
    app.create_emp(31, 'Sunday', 'March')