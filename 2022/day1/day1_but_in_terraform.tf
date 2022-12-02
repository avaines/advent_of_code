locals {
    input = file("input.txt")
    processed_input = split("\n\n", local.input)
    calories_per_elf = [ for snacks in local.processed_input: sum(compact(split("\n", snacks)))]

    # TIL about expansion syntax (...)
    # https://developer.hashicorp.com/terraform/language/expressions/function-calls#expanding-function-arguments
    max_calories_carried = max(local.calories_per_elf...)

    # the list is of strings, so they need padding or it will sort them weirdly, so pad em out to 8 chars 1st
    sorted_calories_per_elf = sort([for elf_calories in local.calories_per_elf: format("%08d", elf_calories)])
    top_3_calories_carried = slice(local.sorted_calories_per_elf, length(local.sorted_calories_per_elf) -3, length(local.sorted_calories_per_elf))
}

output "part1" {
    value = local.max_calories_carried
}

output "part2" {
    value = sum(local.top_3_calories_carried)
}
