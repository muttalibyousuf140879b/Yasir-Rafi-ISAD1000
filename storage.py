import csv

def load_services(filename):
    """
    Load cloud service data from a CSV file.
    :param filename: str, name of the CSV file
    :return: dict, all services with tiers and costs
    """
    services = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)
        for i in range(0, len(lines), 3):
            name, unit = lines[i]
            tiers = list(map(float, lines[i + 1]))
            costs = list(map(float, lines[i + 2]))
            services[name] = {"unit": unit, "tiers": tiers, "costs": costs}
    return services
