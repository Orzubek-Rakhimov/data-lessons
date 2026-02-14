yosh = 17


# if TRUE 
if yosh < 18:
    print("Sizga kirish mumkin emas")
# if False 
elif yosh == 18:
    print("Sizga 10% chegirma bariladi")    
# if FALSE 
else:
    print("Sizga kirish mumkin")
    
    
# kilometrdan -> metra  1
# metra -> kilometrdan  2

    
# 1 Kilometrdan metra
# 5 
# 5000 metr


# 2 Kilometrdan metra
# 2000 
# 2 km

x = int(input("1 yoki 2 ni kirgazing: " ))

if (x == 1):
    y = float(input("Kilometrni kirgizing: "))
else:
    y = float(input("Metrni kirgazing kirgizing: "))

if x == 1:
    print(y*1000,"m")
elif x == 2:
    print(y/1000,"km")
else:
    print("Tanlovni to'gri tanlang!")
    

