import random
import matplotlib.pyplot as plt

def simulate_dice_throws(n_throws):
    sums_freq = {i: 0 for i in range(2, 13)}

    for _ in range(n_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_freq[dice_sum] += 1

    probabilities = {sum_: freq / n_throws for sum_, freq in sums_freq.items()}
    return probabilities

def plot_probabilities(probabilities):
    lists = sorted(probabilities.items())
    x, y = zip(*lists)

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue', edgecolor='black')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    plt.title('Probability of Dice Rolls Sums (Monte Carlo Simulation)')
    plt.xticks(range(2, 13))
    plt.yticks([i/100 for i in range(0, 21, 2)])
    plt.grid(axis='y', linestyle='--')
    plt.show()

n_throws = 1000000
probabilities = simulate_dice_throws(n_throws)

plot_probabilities(probabilities)

print("Simulated Probabilities:")
for sum_, prob in probabilities.items():
    print(f"Sum {sum_}: {prob:.4f} or {prob*100:.2f}%")
