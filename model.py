import random

# Parameters
population_size = 100    # Number of individuals in the population
gene_length = 10         # Number of genes per chromosome
num_chromosomes = 2      # Number of chromosomes in an individual
generations = 50         # Number of generations to simulate
mutation_rate = 0.01     # Probability of mutation per gene
enable_crossing_over = True  # Set to True to enable crossing over

# Function to create an individual with random chromosomes (each chromosome is a list of genes)
def create_individual():
    chromosomes = [[random.randint(0, 1) for _ in range(gene_length)] for _ in range(num_chromosomes)]
    return chromosomes

# Function to create an initial population
def create_population(size):
    return [create_individual() for _ in range(size)]

# Function to reproduce two parents with or without crossing over
def reproduce(parent1, parent2):
    if enable_crossing_over:
        # Simulate crossing over by swapping entire chromosome segments
        crossover_point = random.randint(1, num_chromosomes - 1)  # We crossover between chromosomes, not genes
        child_chromosomes = parent1[:crossover_point] + parent2[crossover_point:]
    else:
        # No crossing over, child gets one chromosome from each parent randomly
        child_chromosomes = [random.choice([parent1[i], parent2[i]]) for i in range(num_chromosomes)]
    
    # Apply mutation to each gene in each chromosome
    for i in range(num_chromosomes):
        for j in range(gene_length):
            if random.random() < mutation_rate:
                child_chromosomes[i][j] = 1 - child_chromosomes[i][j]  # Flip the gene (0 -> 1, or 1 -> 0)
    
    return child_chromosomes

# Function to simulate one generation
def simulate_generation(population):
    new_population = []
    for _ in range(population_size):
        # Select two random parents from the population
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        
        # Create a child and add to the new population
        child = reproduce(parent1, parent2)
        new_population.append(child)
    return new_population

# Function to calculate the frequency of each gene type (0 or 1) in the population
def calculate_gene_pool(population):
    gene_pool = [0] * (num_chromosomes * gene_length)
    for individual in population:
        for chromosome in individual:
            for i, gene in enumerate(chromosome):
                gene_pool[i] += gene
    # Convert counts to frequencies
    return [round(count / (population_size * num_chromosomes), 2) for count in gene_pool]

# Main simulation
population = create_population(population_size)
for generation in range(generations):
    print(f"Generation {generation + 1}")
    
    # Calculate and display gene pool frequencies
    gene_frequencies = calculate_gene_pool(population)
    print("Gene Frequencies:", gene_frequencies)
    
    # Generate the next generation
    population = simulate_generation(population)

print("\nFinal Generation Gene Pool Frequencies:", calculate_gene_pool(population))

