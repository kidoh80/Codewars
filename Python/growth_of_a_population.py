def nb_year(p0, percent, aug, p):
    num_of_years = 0
    num_of_inhabitants = p0
    while (num_of_inhabitants < p):
        num_of_years += 1
        num_of_inhabitants += (num_of_inhabitants * (percent/100)) + aug
    return num_of_years
