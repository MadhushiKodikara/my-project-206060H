import random

# Simulated win-loss data for Sri Lanka (you should replace this with real data)
sri_lanka_wins = 150
sri_lanka_losses = 100

# Function to simulate a match result
def simulate_match():
    return random.choice(["Sri Lanka", "Opponent"])

# Number of simulations to run
num_simulations = 10000

# Initialize counters for Sri Lanka's wins and losses
sri_lanka_wins_count = 0
sri_lanka_losses_count = 0

# Simulate matches and count wins and losses
for _ in range(num_simulations):
    winner = simulate_match()
    if winner == "Sri Lanka":
        sri_lanka_wins_count += 1
    else:
        sri_lanka_losses_count += 1

# Calculate the probability of Sri Lanka winning
probability_sri_lanka_wins = sri_lanka_wins_count / num_simulations

# Calculate the probability of Sri Lanka losing
probability_sri_lanka_losses = sri_lanka_losses_count / num_simulations

print(f"Probability of Sri Lanka winning: {probability_sri_lanka_wins:.2%}")

-------------------------------------------------------------------------------------------------------------------------------

import random

# Simulated win-loss data for Sri Lanka (you should replace this with real data)
sri_lanka_wins = 150
sri_lanka_losses = 100

# Function to simulate a match result
def simulate_match():
    return random.choice(["Sri Lanka", "Opponent"])

# Number of simulations to run
num_simulations = 10000

# Initialize counters for Sri Lanka's wins and losses
sri_lanka_wins_count = 0
sri_lanka_losses_count = 0

# Initialize variables for margin of victory
total_margin_of_victory = 0

# Simulate matches and count wins and losses
for _ in range(num_simulations):
    winner = simulate_match()
    if winner == "Sri Lanka":
        sri_lanka_wins_count += 1
        # Simulate a margin of victory (random value)
        margin_of_victory = random.randint(1, 100)
        total_margin_of_victory += margin_of_victory
    else:
        sri_lanka_losses_count += 1

# Calculate the probability of Sri Lanka winning and losing
probability_sri_lanka_wins = sri_lanka_wins_count / num_simulations
probability_sri_lanka_losses = sri_lanka_losses_count / num_simulations

# Calculate the average margin of victory for Sri Lanka
average_margin_of_victory = total_margin_of_victory / sri_lanka_wins_count if sri_lanka_wins_count > 0 else 0

print(f"Probability of Sri Lanka winning: {probability_sri_lanka_wins:.2%}")
print(f"Probability of Sri Lanka losing: {probability_sri_lanka_losses:.2%}")
print(f"Average margin of victory for Sri Lanka: {average_margin_of_victory:.2} runs")

print(f"Probability of Sri Lanka losing: {probability_sri_lanka_losses:.2%}")
