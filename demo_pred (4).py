#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def demo_prediction(m_4):
    import colorama
    from colorama import Fore,Style
    
    print("Enter the data for the follwing parameters")
    print("Pregnancies:",end=" ")
    q1=int(input())
    print("Glucose:",end=" ")
    q2=int(input())
    print("BloodPressure:",end=" ")
    q3=int(input())
    print("SkinThickness:",end=" ")
    q4=int(input())
    print("Insulin:",end=" ")
    q5=int(input())
    print("BMI:",end=" ")
    q6=float(input())
    print("DiabetesPedigreeFunction:",end=" ")
    q7=float(input())
    print("Age:",end=" ")
    q8=int(input())
    pre=m_4.predict([[q1,q2,q3,q4,q5,q6,q7,q8]])
    print(" ")
    if(pre==1):
        print(Fore.RED+Style.BRIGHT+"Result: Higher level of diabetes risk")
    else:
        print(Fore.GREEN+Style.BRIGHT+"Result: Lower level of diabetes risk")
    return

