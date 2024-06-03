print("LIST OF SHAPES:\n1. Circle\n2. Rectangle\n3. Square\n4. Triangle")
x=input("Select a shape from the given list: ") #takes input from the user
if(x=='1' or x=='Circle' or x=='circle'): #checks the given condition and if stands true will print the given statement
    r=int(input("Enter the radius of the circle: ")) #takes radius as input from user
    area=3.14*r*r 
    circum= 2*3.14*r
    print("The area of circle is", area)
    print("The circumference of the circle is", circum)
elif(x=='2' or x=='rectangle' or x=='Rectangle'):
    l=int(input("Enter length of Rectangle: ")) #takes length as input from user
    b=int(input("Enter breadth of Rectangle: ")) #takes breadth as input from user
    area=l*b
    peri=2*(l+b)
    print("The area of Rectangle is", area)
    print("The perimeter of the Rectangle is", peri)
elif(x=='3' or x=='Square' or x=='square'): 
    s=int(input("Enter the side of the Square: ")) #takes the side as input from user
    area= s*s
    peri= 4*s
    print("The area of Square is", area)
    print("The perimeter of the Square is", peri)
elif(x=='4' or x=='Triangle' or x=='triangle'): 
    print("Enter the sides of triangle:")
    a=int(input("Side a= "))  #take the sides as input from user
    b=int(input("Base b= "))
    c=int(input("Side c= "))
    h=int(input("Enter height of the triangle: "))      #takes the height as input from user   
    area= 0.5*b*h
    peri= a+b+c
    print("The area of Triangle is", area)
    print("The perimeter of the Triangle is", peri)
else:   #if non of the above condition stands true, else statement will be printed
    print("You have entered the wrong choice")
    