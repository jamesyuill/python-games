print('Welcome to my computer quiz!')

playing = input('Do you want to play a game? ')

if playing.lower() != 'yes':
    quit()

print("Okay, let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('wrong chump!')

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('wrong chump!')

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print('correct!')
    score += 1
else:
    print('wrong chump!')

print(f'You got {score} questions correct')
print(f'You got {(score/3) *100}%')