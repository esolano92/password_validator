import tkinter as tk
from tkinter import messagebox


alphabet_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits_list = [0,1,2,3,4,5,6,7,8,9]
special_characters_list = ["!","@","#","$","%","^","&","*","(",")","-","+","=","?","<",">","/","`",":",";"]


def check_length(password):
    if len(password) >= 6 and len(password) <= 24:
        return True
    else:
        print("Incorrect amount of characters in your password. Please try again!")
        return False

def check_for_upper(password):  
    for char in password:
        if char in alphabet_list:
            return True
    
    print("Incorrect amount of uppercase characters in your password.")
    return False

def check_for_lower(password):
    lower_case = []
    for num in range(len(alphabet_list)):
        lower_case.append(alphabet_list[num].lower())
        for char in password:
            if char in lower_case:
                return True

    print("Incorrect amount of lowercase characters in your password.")    
    return False
    
def check_digit(password):
    digit_string_list = []
    for num in range(len(digits_list)):
        digit_string_list.append(str(digits_list[num]))
        for char in password:
            if char in digit_string_list:
                return True

    print("Incorrect amount of digits in your password.")
    return False
    
def check_repitions(password):
    index = 0
    sequence_reps = 1
    while index < len(password) -1:
    
        if password[index] == password[index + 1]:
            sequence_reps += 1
            if sequence_reps == 3:
                print("Too many characters in sequential order.")
                return False
        index += 1
    return True

            
def password_validator(password):
    if check_length(password) and check_for_upper(password) and check_for_lower(password) and check_digit(password) and check_repitions(password):
        messagebox.showinfo("Success!", "Your password has been successfully validated.")
        return True
    else:
        messagebox.showinfo("Please fix the above problems within your password!")
        return False


window = tk.Tk()
window.title("Password Validator")

label = tk.Label(window, text="Enter Password:")
label.pack()

textfield = tk.Entry(window, show="*")
textfield.pack()

button = tk.Button(window, text="Validate", command=lambda: password_validator(textfield.get()))
button.pack()


window.mainloop()
