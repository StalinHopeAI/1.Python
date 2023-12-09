class multiplefunctions():
    def subfields():
        AI_Subfields=["Machine Learning", "Neural Networks Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for Subfield in AI_Subfields:
            print(Subfield)
    def OddEven():
        num=int(input("Enter the Number:"))
        if((num%2)==0):
            print("Given Number is Even ")
            message="Even Number"
        else:
            print("Given Number is Odd")
            message="odd number"
    def Elegible():
        age= int(input("Enter the Age:"))
        gender=(input("Enter the Gender:"))

        if (age>=21 and gender== "Male"):
            print("Elegible")
        elif (age>=18 and gender== "Female"):
            print("Elegible")    
        else:
            print("Not Elegible")
    def percentages():
        subject1=int(input("enter the Subject1:"))
        subject2=int(input("enter the Subject2:"))
        subject3=int(input("enter the Subject3:"))
        subject4=int(input("enter the Subject4:"))
        subject5=int(input("enter the Subject5:"))
        Total=subject1+subject2+subject3+subject4+subject5
        print("Total:",Total)
        print("percentage:",format(Total/5,".12f"))
                                                                            
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        area = ((Height * Breadth)/2)
        print("Area of triangle:", area)
        height1 = int(input("Height1: "))
        height2 = int(input("Height2: "))
        Breadth = int(input("Breadth: "))
        perimeter = height1 + height2 + Breadth
        print("perimeter of triangle:", perimeter)