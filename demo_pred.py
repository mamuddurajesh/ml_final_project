#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def demo_prediction(m_4):
    print("Enter the data for the follwing parameters")
    print("Enter no_preg:",end=" ")
    q1=int(input())
    print("Enter glu_conc:",end=" ")
    q2=int(input())
    print("Enter diasotlic_bp:",end=" ")
    q3=int(input())
    print("Enter thickness:",end=" ")
    q4=int(input())
    print("Enter insuline:",end=" ")
    q5=int(input())
    print("Enter bmi:",end=" ")
    q6=float(input())
    print("Enter dia_pedeg:",end=" ")
    q7=float(input())
    print("Enter age:",end=" ")
    q8=int(input())
    print("Enter skin:",end=" ")
    q9=float(input())
    pre=m_4.predict([[q1,q2,q3,q4,q5,q6,q7,q8,q9]])
    if(pre==1):
        print("Result: Higher level of diabetes risk")
    else:
        print("Result: Lower level of diabetes risk")
    return

