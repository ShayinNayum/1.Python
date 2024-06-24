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

       
        def Elegible():
            gender=(input("your Gender: "))
            age=int(input("your Age:"))
            if(gender=="Male"and age>21):
                print("Eligible")
                Eligible="Eligible"
            elif(gender=="Female"and age>18):
                print("Eligible")
                Eligible="Eligible"
            else:
                print("not Eligible")
                Eligible="not Eligible"
                return Eligible

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
            
            height=int(input("Height:"))
            breadth=int(input("Breadth:"))
            Area_formula=(height*breadth)/2
            print("Area formula : (Height*Breadth)/2")
            print("Area of Triangle ",Area_formula)

            Height1=int(input("Height1 :"))
            Height2=int(input("Height2 :"))
            Breadth=int(input("Breadth :"))
            Preimeter_formula= Height1+Height2+Breadth
            print("Preimeterformula= Height1+Height2+Breadth")
            print("Preimeter of Triangle",Preimeter_formula)

            return Triangle()