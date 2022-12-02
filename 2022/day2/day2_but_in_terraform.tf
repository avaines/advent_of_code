locals {
    input = file("input.txt")
    processed_input = split("\n", local.input)

    score_lookup = {
        "A X" = 1+3
        "A Y" = 2+6
        "A Z" = 3+0
        "B X" = 1+0
        "B Y" = 2+3
        "B Z" = 3+6
        "C X" = 1+6
        "C Y" = 2+0
        "C Z" = 3+3
    }

/*
A B C is still R P S
X Y Z is now must lose, draw, win
*/
    score_calculated_lookup = {
        "A X" = local.score_lookup["A Z"] # lose
        "A Y" = local.score_lookup["A X"] # draw
        "A Z" = local.score_lookup["A Y"] # win
        "B X" = local.score_lookup["B X"] # lose
        "B Y" = local.score_lookup["B Y"] # draw
        "B Z" = local.score_lookup["B Z"] # win
        "C X" = local.score_lookup["C Y"] # lose
        "C Y" = local.score_lookup["C Z"] # draw
        "C Z" = local.score_lookup["C X"] # win
    }

}

output "part1" {
    value = sum([ for round in local.processed_input: local.score_lookup[round]])
}

output "part2" {
    value = sum([ for round in local.processed_input: local.score_calculated_lookup[round]])
}