def greedy_algorithm(items, budget):
    ratios = {item: (details["calories"] / details["cost"]) for item, details in items.items()}
    sorted_items = sorted(ratios, key=ratios.get, reverse=True)

    chosen_items = {}
    total_calories = 0
    for item in sorted_items:
        if items[item]["cost"] <= budget:
            chosen_items[item] = items[item]
            budget -= items[item]["cost"]
            total_calories += items[item]["calories"]

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.keys())

    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_list[i-1]]["cost"] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-items[item_list[i-1]]["cost"]] + items[item_list[i-1]]["calories"])
            else:
                dp[i][w] = dp[i-1][w]

    chosen_items = {}
    total_calories = dp[len(items)][budget]
    w = budget
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items[item_list[i-1]] = items[item_list[i-1]]
            w -= items[item_list[i-1]]["cost"]

    return chosen_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Test
budget = 100
print("Greedy algorithm:")
chosen_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(chosen_greedy, total_calories_greedy)

print("\nDynamic Programming:")
chosen_dp, total_calories_dp = dynamic_programming(items, budget)
print(chosen_dp, total_calories_dp)
