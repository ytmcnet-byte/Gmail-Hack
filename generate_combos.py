import itertools

prefix = "murli"
digits = "1234567890"

print("Passwords generate ho rahe hain, kripya intezaar karein...")

with open("password.txt", "w") as f:
    # Total length 7 se 14 characters ke liye 
    # (murli = 5 chars, isliye digits ki length 2 se 9 tak hogi)
    for total_len in range(7, 15):
        digit_len = total_len - len(prefix)
        for combo in itertools.product(digits, repeat=digit_len):
            password = prefix + "".join(combo)
            f.write(password + "\n")

print("Sabhi combinations successfully 'password.txt' mein save ho gaye hain!")
