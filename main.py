# h="hreem"
# print(h[:])
# # slicing
# h={"a":12}
# # a is a
# h["w"]=14
# # print(h["hareem"])
# print(h.get("hareem"))
# print(h.keys())
# print(h)
# print(h.items())
# for i in range(5):
#     print(i)
#     # print(i,i*
# marks=[1,2,3,4]
# for item in marks:
#     print(item)
# while(True):
#     a=input("who is best? ")
#     if(a=="arfa"):
#         print("you are right!")
#     else:
#         print("amazing but not best")
# try:
#     n=int(input("enter a number please"))
#     print(n,"is a number,great!")
#
# except Exception as e:
#     print("you nned to know what number is.. huh, \nerror occured\n",e)
#short method
with open("FileHandling.txt","w") as f:
    f.write("Hareem is back to programming")
#context  method to make a file - long method have to close
fp=open("newFile.txt","w")
fp.write("she is amazing")
fp.close()
with open("newFile.txt","r") as f:
    s=f.read()
    print(s)
with open("FileHandling.txt","a") as f:
    f.write("Hareem is doing great")