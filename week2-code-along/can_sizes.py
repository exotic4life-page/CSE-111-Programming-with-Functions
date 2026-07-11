# ##Core_requirement
# #Import the standard math module so that
# # math.pi can be used in this program.
# import math

# #This function computes and prints the storage efficiency for each of the following 12 steel can sizes.
# def main():
#     name = "#picnic1"
#     radius = 6.83
#     height = 10.16
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#1 Tall"
#     radius = 7.78
#     height = 11.91
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#2"
#     radius = 8.73
#     height = 11.59
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#2.5"
#     radius = 10.32
#     height = 11.91
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#3 Cylinder"
#     radius = 10.79
#     height = 17.78
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#5"
#     radius = 13.02
#     height = 14.29
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#6Z"
#     radius = 5.40
#     height = 8.89
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#8Z short"
#     radius = 6.83
#     height = 7.62
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#10"
#     radius = 15.72
#     height = 17.78
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#211"
#     radius = 6.83
#     height = 12.38
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#300"
#     radius = 7.62
#     height = 11.27
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

#     name = "#303"
#     radius = 8.10
#     height = 11.11
#     volume = compute_volume(radius, height)
#     surface_area = compute_surface_area(radius, height)
#     storage_efficiency = volume / surface_area
#     print(f"{name} {storage_efficiency:.2f}")

# #This function compute/calculates the volume of a can
# def compute_volume(radius, height):
#     volume = math.pi * radius * radius * height
#     return volume


# #This function compute the surface area of a can 
# def compute_surface_area(radius, height):
#     surface_area = 2 * math.pi * radius * (radius + height)
#     return surface_area

# # Start this program by
# # calling the main function.
# main()


##Stretch_challenge
import math


def main():
    # Four parallel lists, one list for each attribute of the cans.
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the parallel lists, unpack the values
    # into the variables name, radius, height, and cost.
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]

        # Call the compute_storage_efficiency and
        # compute_cost_efficiency functions.
        store_eff = compute_storage_efficiency(radius, height)
        cost_eff  = compute_cost_efficiency(radius, height, cost)

        # Print the can size name, storage
        # efficiency, and cost efficiency.
        print(f"{name} {store_eff:.2f} {cost_eff:.0f}")

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

    # Print the best storage and cost efficiencies.
    print()
    print("Best can size in storage efficiency:", best_store)
    print("Best can size in cost efficiency:", best_cost)


def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency
    
def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    efficiency = volume / cost
    return efficiency


def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area


# Start this program by
# calling the main function.
main()