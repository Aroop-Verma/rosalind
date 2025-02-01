def probability_of_dominant_phenotype(k, m, n):
    # Total population
    total = k + m + n

    # Probability of selecting two organisms and having each mating pair:
    # AA x AA
    prob_AA_AA = (k / total) * ((k - 1) / (total - 1))
    
    # AA x Aa
    prob_AA_Aa = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    
    # AA x aa
    prob_AA_aa = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    
    # Aa x Aa
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1))
    
    # Aa x aa
    prob_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))
    
    # aa x aa
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1))

    # Probability of producing dominant phenotype from each pair
    dominant_prob_AA_AA = 1  # 100%
    dominant_prob_AA_Aa = 1  # 100%
    dominant_prob_AA_aa = 1  # 100%
    dominant_prob_Aa_Aa = 0.75  # 75%
    dominant_prob_Aa_aa = 0.5  # 50%
    dominant_prob_aa_aa = 0  # 0%

    # Total probability of producing a dominant phenotype
    total_dominant_prob = (
        prob_AA_AA * dominant_prob_AA_AA +
        prob_AA_Aa * dominant_prob_AA_Aa +
        prob_AA_aa * dominant_prob_AA_aa +
        prob_Aa_Aa * dominant_prob_Aa_Aa +
        prob_Aa_aa * dominant_prob_Aa_aa +
        prob_aa_aa * dominant_prob_aa_aa
    )
    
    return round(total_dominant_prob, 5)

# Example usage
k, m, n = 27, 27, 17
result = probability_of_dominant_phenotype(k, m, n)
print(result)
