num          = 0
input_status = "invalid"

while input_status == "invalid" :
    try:
        num = int(input("Enter a number : "))
        print("Number entered", num)
        input_status = "valid"
    except:
        print("Enter a interger number")
