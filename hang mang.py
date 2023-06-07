# ------ hang mang بازی -------
import random

# 1=kalameh be sort random entakhab mikonim
words = ["قرمز", "مبل", "فرش", "موز", "قابلمه", "لیوان", "پارچ", "ریاضی", "خط"]  # tedad kalameh mord nazar tarif mikonm
answer = random.choice(words)
print(answer)

# 2=tedad horof tashkhis midam--------------------------------------------------------------

tedad_harf = 0
for i in answer:
    tedad_harf += 1
print(tedad_harf)
khatha = tedad_harf * "_"
print(khatha)

# 3=  be list tabdil mikonim-----------------------------------------------------------------


khatha_answer = list(khatha)
print(khatha_answer)



# 4= 2 halat darim :ya harf vared mishavad dorst hast ya na----------------------------------


y = input("یک حرف وارد کنید")
x = ""
while "_" in khatha_answer:
    x = ""
    if y in answer:  # اگر حرف که وارد کردیم درست باشه
        for j in range(0, len(answer)):
            if answer[j] == y:
                khatha_answer[j] = answer[j]
            x = x + khatha_answer[j]
        print(x)
        if "_" in khatha_answer:
            y = input("یک حرف دیگه وارد کن")
        else:
            print("شما برنده شده اید :) ")
            break;
    else:  # اگر حرف که وارد کردیم  درست نباشد
        y = input("یک حرف دیگه وارد کنید")
