# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# Rock = 1, Paper = 2, Scissors = 3
# Loss = 0, Draw = 3, Win = 6

scoring = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def win_loss_draw(them, you) -> int:
    match them:
        case "A":
            #Opponent picked rock, we can draw if we picked rock, win if we picked paper and lose if we picked scissors
            match you:
                case "X":
                    return 1
                case "Y":
                    return 2
                case "Z":
                    return 0
        case "B":
            #Opponent picked paper, we can draw if we picked paper, win if we picked scissors and lose if we picked rock
            match you:
                case "X":
                    return 0
                case "Y":
                    return 1
                case "Z":
                    return 2
        case "C":
            #Opponent picked scissors, we can draw if we picked scissors, win if we picked rock and lose if we picked paper
            match you:
                case "X":
                    return 2
                case "Y":
                    return 0
                case "Z":
                    return 1


def run_round(choices) -> int:
    score = 0
    #Find if we won/lost/draw
    match win_loss_draw(choices[0], choices[1]):
        case 0:
            #Lost
            pass
        case 1:
            #Draw
            score += 3
        case 2:
            #Won
            score += 6
    #Also add the score of the chosen item
    score += scoring[choices[1]]
    return score

with open('input.txt') as f:
    data = f.read().split("\n")
data = data[:-1]

total_score = 0

for line in data:
    choices = line.split(" ")

    total_score += run_round(choices)


print(total_score)

#Part TWO
#Changes, column 2 = what the result needs to be
#X = lose, Y = draw, Z = win
# A = Rock, B = Paper, C = Scissors
total_score = 0

for line in data:
    choices = line.split(" ")

    #Modify choices so I can use same logic from part 1 to calc scores
    match choices[1]:
        case "X":
            #Must lose
            match choices[0]:
                case "A":
                    choices[1] = "Z"
                case "B":
                    choices[1] = "X"
                case "C":
                    choices[1] = "Y"
        case "Y":
            #Must Draw
            match choices[0]:
                case "A":
                    choices[1] = "X"
                case "B":
                    choices[1] = "Y"
                case "C":
                    choices[1] = "Z"
        case "Z":
            #Must Win
            match choices[0]:
                case "A":
                    choices[1] = "Y"
                case "B":
                    choices[1] = "Z"
                case "C":
                    choices[1] = "X"

    total_score += run_round(choices)

print(total_score)