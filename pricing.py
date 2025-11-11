def calculate_cost(service_name, usage, tiers, costs):
    """
    Calculate total monthly cost for a service based on usage and tier pricing.
    :param service_name: str, name of the service
    :param usage: float, amount of service used
    :param tiers: list of float, starting limits for each tier
    :param costs: list of float, cost per unit for each tier
    :return: float, total cost
    """
    total_cost = 0
    for i in range(len(tiers)):
        start = tiers[i]
        end = tiers[i + 1] if i + 1 < len(tiers) else float('inf')

        if usage > start:
            units_in_tier = min(usage, end) - start
            total_cost += units_in_tier * costs[i]
        else:
            break
    return round(total_cost, 2)
