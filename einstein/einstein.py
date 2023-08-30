def calculate_energy(mass):
    speed_of_light = 3e8  # Speed of light in m/s
    energy = mass * (speed_of_light ** 2)
    return int(energy)

def main():
    mass = int(input("Enter mass (in kilograms): "))
    energy = calculate_energy(mass)
    print(energy)

if __name__ == "__main__":
    main()
