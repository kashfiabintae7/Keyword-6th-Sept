print('\033c')

def dueamount (b,g):
    return g - b


bill = int(input("Enter Your Bill: "))
given = int(input("Enter Your Given Amount: "))


due = dueamount(bill, given)

print(f"Bill: {bill}\nGiven: {given}\nDue Amount = {due}")