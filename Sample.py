class std:
    def __init_(self,name,Phn_no,fav1,fav2):
        self.name=name
        self.phn_no=phn_no
        self.fav1=fav1
        self.fav2=fav2

    def display(self):
        print("\n  ***DETAILS OF THE PERSON***")
        print("\nName of the person-",std.name)
        print(std.name,"phn_num-",std.phn_no)
        print(std.name,"Fav food item-",std.fav1)
        print(std.name,"Fav game-",std.fav2)


    name=input("Enter the name:")
    phn_no=int(input("Enter the phn_num:"))
    fav1=input("Enter the Favourite item:")
    fav2=input("Enter the Favourite game:")
        

s1=std()
s1.display()

