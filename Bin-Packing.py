def BinPacking(capacities, max_capacity):
    # the bins are created on the run time
    solution_bins = []
    # [[item3],[item5,item2],[item4,item6],[item1]]
    # print(capacities)

    item_names = list(capacities.keys())
    sorted_items = sorted(item_names, key=lambda x: capacities[x], reverse=1)
    # sorting items in descending order
    print("sorted order of the items:", sorted_items)

    for item in sorted_items:
        binFound = False
        item_capacity = capacities[item]

        # inserting items in the bin
        for index, actual_bin in enumerate(solution_bins):
            actual_bin_summed_size = sum([capacities[key] for key in actual_bin])
            if item_capacity <= (max_capacity - actual_bin_summed_size):
                solution_bins[index].append(item)
                binFound = True
                break

        # if a bin is full then creating a new bin
        if not binFound:
            solution_bins.append([item])
    return solution_bins


items = {"item 1": 4, "item 2": 2, "item 3": 7, "item 4": 5, "item 5": 6, "item 6": 3}
max_capacity = 8
print(BinPacking(items, max_capacity))
