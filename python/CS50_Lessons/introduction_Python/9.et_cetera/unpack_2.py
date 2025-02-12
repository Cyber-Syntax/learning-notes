def total(galleons, sickles, knuts):
    """
    This function calculates the total number of knuts given the number of galleons, sickles, and knuts.
    The conversion rate is: 1 galleon = 17 sickles and 1 sickle = 29 knuts.
    
    :param galleons: Number of galleons
    :type galleons: int
    :param sickles: Number of sickles
    :type sickles: int
    :param knuts: Number of knuts
    :type knuts: int
    :return: Total number of knuts
    :rtype: int
    """
    
    # convert galleons and sickles to knuts and add the number of knuts
    return (galleons * 17 + sickles) * 29 + knuts

# create a list of coins
coins = [100, 50, 25]

# create a dictionary with keys "galleons", "sickles", and "knuts" and values corresponding to the coin amounts
coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}

# print the total number of knuts using the values in the coins list as arguments to the total function
print(total(*coins), "Knuts_list")

# print the total number of knuts using the values in the coins_dict as arguments to the total function
print(total(**coins_dict), "Knuts_dict")
