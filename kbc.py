print("NOTE: Type only the name of person in answer. (Thankyou)")
Que=[1,2,3,4,5,6]

Ans=["Draupti Murmu","Joe Biden","Elon Musk","Parag Aggarwal","Bill Gates","Steve Jobs"]
def line():
  print("\n--------------------------------------------------\n")
def check(x):
  Que[x]=input("Enter your Answer:-")# After this we define Que[x] as the real question. And then match it with Ans[x].
  if Que[x]==Ans[x]:
    print("\nResult-Great Job, Your Answer is Right.")
  else:
    print("\nResult-Oh NO.You are wrong.")

Que[0]=print('''\nQue.1 Who is the president of our country ?
     a. Draupti Murmu         b.Modi
     c.Joe Biden              d.Harry Bhai
''')
check(0)
line()


Que[1]=print('''\nQue.2 Who is the president of U.S.A ?
     a. Daunald Trump           b.Narendra Modi
     c. Joe Biden               d.Barack Obama
''')
check(1)
line()


Que[2]=print('''\nQue.3 Who is the current CEO of Twitter ?
     a. Parag Aggarwal             b. Warren Buffet
     c. Jeff Bezos                 d. Elon Musk
''')
check(2)
line()


Que[3]=print('''\nQue.4 Who is the previous CEO of Twitter ?
     a. Warren Buffet              b. Parag Aggarwal
     c. Jeff Bezos                 d. Elon Musk
''')
check(3)
line()


# SOLVE THIS
if Que[0:3]==Ans[0:3]:
  print("Yeah, You almost near to clear the first level.")
else:
    print("Be Aware, You are not doing well.")
line()
Que[4]=print('''\nQue.5 Who is the Founder of Microsoft ?
     a. Bill Gates                 b. Warren Buffet
     c. Jeff Bezos                 d. Elon Musk
''')
check(4)
line()


Que[5]=print('''\nQue.6 Who is the Founder of Apple ?
     a. Bill Gates                 b. Warren Buffet
     c. Steve Jobs                 d. Elon Musk
''')
check(5)
line()


if Que>=Ans[0:4]:
  a=print("You passed the exam; Now Come to next level.Before coming to the next level, We have to give you a cheque of ₹10,000\n")
else:
  print("OH NO !, You are not qualified to the next level. Don't be sad. No matter you wins or not you have to be play for just increasing your knowledge.\n")
line()
line()
if Que>=Ans[0:4]:
    Que_next=[7,8,9,10,11,12]
    Ans_next=["24 February 1955","Both of all","T series","IT industry","Apple","Reliance"]
  
    def check_next(x):
      Que_next[x]=input("Enter your Answer:-")
      if Que_next[x]==Ans_next[x]:
        print("\nResult-Great Job, Your Answer is Right.")
      else:
        print("\nResult-Oh NO.You are wrong.")
    
    Que_next[0]=print('''\nQue.7 When was Steve Jobs born ?
     a. 24 March 1955               b. 24 February 1956
     c. 24 February 1955            d. 23 October 1955
    ''')
    check_next(0)
    line()
  
    Que_next[1]=print('''\nQue.8 Who was the founder of Youtube?
     a. Jawed Karim                 b. Steve Chen
     c. Chad Hurley                 d. Both of all
    ''')
    check_next(1)
    line()

    Que_next[2]=print('''\nQue.9 Which Youtube channel has most subscribers in the world?
     a. Cocummelon                  b. Zee Music
     c. Sony T.V                    d. T series
    ''')
    check_next(2)
    line()

    Que_next[3]=print('''\nQue.10 Which industry is often called the backbone of country ? 
    a. Iron and Steel industry       b. IT industry
    c. Textile Industry              d. Oil industry 
    ''')
    check_next(3)
    line()
    Que_next[4]=print('''\nQue.11 Which tech company has largest market value in the world ? 
    a. Microsoft        b. Google
    c. Apple            d.  Facebook
    ''')
    check_next(4)
    line()
    print("\nHowever, You wonder to hear that it's market value is 2.8 trillion dollar which is more than the GDP of India.")
    line()
    Que_next[5]=print('''\nQue.12   Which tech company has largest market value in the India?
    a. Tata Consultacy service        b. Reliance
    c. Infosys                        d. HDFC bank
    ''')
    check_next(5)
    line()
# I can't solve it.==>
# if Que_next==Ans_next:
#   print("You acieve this,now you are qualified to the third and the final level")
# else:
#   print("You did better but it's time for giving the final cheque of ₹",len(Que_next)*10000)
