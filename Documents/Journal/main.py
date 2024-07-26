#file = open(r"C:\Users\omarh\Desktop\members.txt", "r")
#Members=file.readlines()
#print(Members)


#New_member=input("Add a new member:") + "\n"
#Members.append(New_member)
#file = open(r"C:\Users\omarh\Desktop\members.txt", "w")
#file.writelines(Members)
#file.close()

#filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#for i in filenames:
#    file=open(f"{i}","w")
#    file.write('Hello')

#filenames=['a.txt' , 'b.txt' , 'c.txt']
#for i in filenames:
#    file=open(rf"C:\Users\omarh\Desktop\{i}","r")
#    print(file.read())
#file = open("data.txt", 'w')

#file.write("100.12" +"\n")
#file.write("111.23")
#file.writelines(["100.12" +"\n", "111.23"])
#file.close()

Date = input("Enter today's date")
Mood = input("How do you rate your mood today from 1 to 10?")
Mo = input("Let your thought flow:")

with open(rf"C:\Users\omarh\PycharmProjects\pythonProject1\Documents\Journal\{Date}.txt","w") as file:
    file.write(Mo)
with open(rf"C:\Users\omarh\PycharmProjects\pythonProject1\Documents\Journal\{Date}.txt","r") as file:
    print(file.read())
    print(file.read())