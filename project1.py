sal=float(input("enter employee salary:"))
sp1=float(input("enter shopping bill1:"))
sp2=float(input("enter shopping bill2:"))
sp3=float(input("enter shopping bill3:"))
total=sp1+sp2+sp3
per=(total/sal)*100
print(total)
print("amount spent on shopping in percentage: ",per,"%")