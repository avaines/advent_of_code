locals {
    input = file("sample.txt")
    processed_input = split("\n", local.input)

    score_lookup = {
        "A X" = 1+3
        "A Y" = 2+6
        "A Z" = 3+3
        "B X" = 1+0
        "B Y" = 2+3
        "B Z" = 3+6
        "C X" = 1+6
        "C Y" = 2+0
        "C Z" = 3+3
    }

    the_game = sum([ for round in local.processed_input: local.score_lookup[round]])

}

output "part1" {
    value = local.the_game
}

