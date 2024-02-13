import math
import time


def resultant(magnitudes, bearings):
    x_sum = 0
    y_sum = 0

    for magnitude, bearing in zip(magnitudes, bearings):
        angle_rad = math.radians(bearing)
        x_sum += magnitude * math.cos(angle_rad)
        y_sum += magnitude * math.sin(angle_rad)

    final_mag = math.sqrt(x_sum ** 2 + y_sum ** 2)
    final_angle = math.degrees(math.atan2(y_sum, x_sum))
    if final_angle < 0:
        final_angle += 360

    return final_mag, final_angle


number_of_vectors = int(input('How many vectors do you have: '))
vectors_magnitudes = []
vectors_bearings = []
for i in range(number_of_vectors):
    temp_mag = float(input(f'Enter the magnitude of vector {i + 1}: '))
    vectors_magnitudes.append(temp_mag)
    temp_bearing = float(input(f'Enter the bearing of vector {i + 1}: '))
    vectors_bearings.append(temp_bearing)

resultant_vector = resultant(vectors_magnitudes, vectors_bearings)
print(f'Resultant Vector: {resultant_vector[0]} on a bearing of {resultant_vector[1]}')
time.sleep(10)
