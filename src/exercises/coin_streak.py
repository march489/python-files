import random

number_of_streaks = 0

for experiment_number in range(10000):
    # code that creates a list of 100 'heads' or tails'
    experiment = [random.randint(0,1) for item in range(100)]

    # code that checks if there's a streak of 6 or more heads or tails in a row. 
    current_streak = 1
    for index, flip in enumerate(experiment):
        if index == 0:
            continue
        else: 
            if flip == experiment[index - 1]:
                current_streak += 1
                if current_streak == 6:
                    number_of_streaks += 1
                    break
            else: 
                current_streak = 1

print('Chance of streak: %s%%' %(number_of_streaks // 100))