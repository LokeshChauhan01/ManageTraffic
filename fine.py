def calculate_average_speed(distance, time):
    return (distance / time)

def apply_fine(speed_limit, recorded_speed):
    if recorded_speed <= speed_limit:
        return 0
    else:
        fine = (recorded_speed - speed_limit) * 10
        return fine

def main():
    # Assuming the data from traffic cameras is stored as a list of tuples,
    # where each tuple contains the distance (in meters) and time (in seconds) of a vehicle passing a camera.
    # Example: data = [(distance1, time1), (distance2, time2), ...]
    data = [(1000, 30), (1200, 35), (800, 20)]

    total_distance = 0
    total_time = 0

    for distance, time in data:
        total_distance += distance
        total_time += time

    average_speed = calculate_average_speed(total_distance, total_time)

    speed_limit = 60  # Set the speed limit in km/h

    fine = apply_fine(speed_limit, average_speed)

    print("Average Speed:", average_speed, "km/h")
    print("Fine:", fine, "$")

if __name__ == '__main__':
    main()
