import matplotlib.pyplot as plt

def fibonacci_rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rabbits(n-1, k) + k * fibonacci_rabbits(n-2, k)

def plot_rabbit_population(n, k, rabbit_pairs):
    months = range(1, n+1)
    fig, ax = plt.subplots()
    ax.plot(months, rabbit_pairs, 'b-', linewidth=2)
    ax.set_xlabel('Months')
    ax.set_ylabel('Rabbit pairs')
    ax.set_title(f'Growth of rabbit population over {n} months with k={k}')
    plt.show()

# Prompt the user to enter the number of months and the rabbit reproduction factor k
n = 28
k = 3

# Calculate the number of rabbit pairs after n months
rabbit_pairs = []
for i in range(1, n+1):
    rabbit_pairs.append(fibonacci_rabbits(i, k))

# Plot the growth of the rabbit population using Matplotlib
plot_rabbit_population(n, k, rabbit_pairs)
