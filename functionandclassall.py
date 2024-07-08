class multiple():
        
        def subfield():
            AI_field=("machine learning","Neural Networks","vision,robotics","speach Processing","Natural Language Processing")
            print("Sub-fields in AI are:")
            for subfield in AI_field:
                print(subfield)
      
        def OddEven():
            num=int(input("enter a number:"))
            if(num%2)==0:
                meg=print(num," is even number")
            else:
                meg=print(num,"is odd number")
                return meg
       
        def Eligible():
            gender = input("Your Gender: ")
            age = int(input("Your Age: "))

            if gender == "Male" and age >= 21:
                print("Eligible")
                eligibility = "Eligible"
            elif gender == "Female" and age >= 18:
                print("Eligible")
                eligibility = "Eligible"
            else:
                print("Not Eligible")
                eligibility = "Not Eligible"

            return eligibility

        def Precentage():
            subject1=int(input("sunject1= "))
            subject2=int(input("sunject2= "))
            subject3=int(input("subject3= "))
            subject4=int(input("subject4= "))
            subject5=int(input("subject5= "))
            total=subject1+subject2+subject3+subject4+subject5
            print("total", total)
            precentage= (total/500)* 100
            print("precentage:", precentage)
            return precentage

        def Triangle():
            # Calculate Area
            height = int(input("Enter the height of the triangle: "))
            breadth = int(input("Enter the breadth of the triangle: "))
            area = (height * breadth) / 2
            print("Area formula: (Height * Breadth) / 2")
            print("Area of the triangle:", area)
            # Calculate Perimeter
            height1 = int(input("Enter the first side length of the triangle: "))
            height2 = int(input("Enter the second side length of the triangle: "))
            breadth = int(input("Enter the base length of the triangle: "))
            perimeter = height1 + height2 + breadth
            print("Perimeter formula: Side1 + Side2 + Base")
            print("Perimeter of the triangle:", perimeter)