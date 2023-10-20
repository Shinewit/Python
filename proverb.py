from math import pow
# pow(1.01,3),pow(0.99,2)
if (pow(1+0.01,3)*pow(1-0.01,2) ) < 1.01:
    print("三天打鱼两天晒网，等于一场空！！")
else:
    print("晒网险胜一筹！！！")