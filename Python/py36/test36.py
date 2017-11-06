def convert_to_numeric(input):
    """
    Try to conver the input to float,
    if it is a string convert the string to return the float number
    """
    try:
        val = float(input)
    except ValueError:
        print("in exception")
        input = input.lower()
        if input == "one":
            val = 1
        elif input == "two":
            val = 2
        elif input == "three":
            val = 3
        elif input == "four":
            val = 4
        elif input == "five":
            val = 5
        else:
            val = -1
    return val


def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5,
    into a rating.
    """
    if av_score < 1:
        return "Terrible"
    elif av_score < 2:
        return "Bad"
    elif av_score < 3:
        return "OK"
    elif av_score < 4:
        return "Good"
    else:
        return "Excellent"


def scores_to_rating(score1, score2, score3, score4, score5):
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)
    av_score = ((sum_of_middle_three(score1, score2, score3, score4, score5)) / 3)
    rating = score_to_rating_string(av_score)
    return rating


test = scores_to_rating(1, "2", "3.0", 4, 5)
print(test)

# #First Example - uncomment lines or change values to test the code
# phone_balance = 7.62
# bank_balance = 104.39
# #phone_balance = 12.34
# #bank_balance = 25
# if phone_balance < 10:
#     phone_balance += 10
#     bank_balance -= 10
# print(phone_balance)
# print(bank_balance)
#
# #Second Example
#
# #change the number to experiment!
# number = 145346334
# #number = 5 #3 sir
# if number % 2 == 0:
#     print("The number " + str(number) + " is even.")
# else:
#     print("The number " + str(number) + " is odd.")
#
# #Third Example
#
# #change the age to experiment with the pricing
# age = 35
#
# #set the age limits for bus fares
# free_up_to_age = 4
# child_up_to_age = 18
# senior_from_age = 65
#
# #set bus fares
# concession_ticket = 1.25
# adult_ticket = 2.50
#
# #ticket price logic
# if age <= free_up_to_age:
#     ticket_price = 0
# elif age <= child_up_to_age:
#     ticket_price = concession_ticket
# elif age >= senior_from_age:
#     ticket_price = concession_ticket
# else:
#     ticket_price = adult_ticket
# message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
# print(message)
#
