def rec_coin(target, coins):

    # Default value set to target
    min_coins = target

    # Checks t see if target is in coin value list
    if target in coins:
        return 1

    else:
        # For every coin value that is <= my target
        for i in [c for c in coins if c <= target]:

            # Add a coin count + Recursive
            num_coins = 1 + rec_coin(target-1, coins)

            # Reset minimum is the new num_coins less than min_coins
            if num_coins < min_coins:

                min_coins = num_coins
    
    return min_coins

def rec_coin_dynam(target, coins, know_results):

    # Default value set to target
    min_coins = target

    # Base case
    if target in coins:
        know_results[target] = 1
        return 1

    # Return a know result if it happens to be geater than 1
    elif know_results[target] > 0:
        return know_results[target]
    
    else:

        #For every coin value that is <= target
        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin_dynam(target-1, coins, know_results)

            if num_coins < min_coins:

                min_coins = num_coins

                # Reset that know result
                know_results[target] = min_coins

    return min_coins    


target = 15
coins = [1, 5, 10, 25]
known_results = [0]*(target+1)

print( rec_coin_dynam(target, coins, known_results))