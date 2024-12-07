import random

# Parameters
population_size = 300    # Number of individuals in the population
gene_length = 50         # Number of genes per chromosome
num_chromosomes = 2      # Number of chromosomes in an individual
generations = 350         # Number of generations to simulate
mutation_rate = 0.005     # Probability of mutation per gene
enable_crossing_over = False  # Set to True to enable crossing over

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
        child_chromosomes = []
        for chrom1, chrom2 in zip(parent1, parent2):
            if random.random() < 0.5:  # Perform crossover with 50% probability per chromosome
                crossover_point = random.randint(1, gene_length - 1)
                child_chromosome = chrom1[:crossover_point] + chrom2[crossover_point:]
            else:
                child_chromosome = random.choice([chrom1, chrom2])  # No crossover
            child_chromosomes.append(child_chromosome)
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

def calculate_gene_pool(population):
    gene_pool = [0] * (num_chromosomes * gene_length)
    for individual in population:
        for chrom_idx, chromosome in enumerate(individual):
            for gene_idx, gene in enumerate(chromosome):
                overall_index = chrom_idx * gene_length + gene_idx
                gene_pool[overall_index] += gene
    return [round(count / (population_size * num_chromosomes), 2) for count in gene_pool]


def calculate_pairwise_distance(population):
    num_individuals = len(population)  # Number of individuals in the population
    total_distance = 0  # Total distance accumulator
    comparisons = 0  # Counter for number of pairs compared

    # Compare each pair of individuals (i, j) where i < j
    for i in range(num_individuals):
        for j in range(i + 1, num_individuals):  # Ensure no self-comparison
            distance = 0  # Reset the distance for each pair of individuals

            # Compare corresponding genes of both individuals
            for chrom1, chrom2 in zip(population[i], population[j]):  # Compare chromosomes
                for gene1, gene2 in zip(chrom1, chrom2):  # Compare corresponding genes
                    distance += abs(gene1 - gene2)  # Calculate absolute difference

            total_distance += distance  # Add the distance for this pair to the total
            comparisons += 1  # Increment the pair counter

    # Calculate the average distance across all pairs
    return total_distance / comparisons if comparisons > 0 else 0

if __name__ == "__main__":
    # Main simulation
    population = create_population(population_size)
    for generation in range(generations):
        print(f"Generation {generation + 1}")

        # Calculate and display gene pool frequencies
        gene_frequencies = calculate_gene_pool(population)
        print("Gene Frequencies:", gene_frequencies)

        # Generate the next generation
        population = simulate_generation(population)


    gene_pool = calculate_gene_pool(population)

    pairwise_distance =  calculate_pairwise_distance(population)

    print(f"pairwise value: {pairwise_distance}")



