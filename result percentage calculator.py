print("Welcome to the the Result Percentage Calculator!")
total_subject=5
sub1=int(input("Enter the Maths Mark :"))
sub2=int(input("Enter the Science Mark :"))
sub3=int(input("Enter the Hindi Mark :"))
sub4=int(input("Enter the English Mark :"))
sub5=int(input("Enter the Social Science Mark :"))
total_of_all_subject=int(100*total_subject)
print(f"Maximam Mark ={total_of_all_subject}")
total_mark_obtain=int(sub1+sub2+sub3+sub4+sub5)
print(f"Total Marks Obtained= {total_mark_obtain}")
percentage= float(total_mark_obtain/total_of_all_subject*100)
Final_percentage=round(percentage,2)
print(f"percentage= {Final_percentage}%")