import random as rd
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
def otp(length):
    """
    this function generates a vrification code

    param:length of code 

    type: int

    return: vrification code
    rtype: str
    """
    password=""
    for _ in range(length):
        password+= rd.choice(characters)
    print(f"generated password: {password}")
    return 
