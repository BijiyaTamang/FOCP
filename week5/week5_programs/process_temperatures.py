import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperatures provided.")
        return

    temperatures = list(map(float, temperatures))
    temperatures_fahrenheit = [celsius_to_fahrenheit(temp) for temp in temperatures]

    max_temp = max(temperatures_fahrenheit)
    min_temp = min(temperatures_fahrenheit)
    mean_temp = sum(temperatures_fahrenheit) / len(temperatures_fahrenheit)

    print("\nResults:")
    print(f"Maximum Temperature: {max_temp:.2f}°F")
    print(f"Minimum Temperature: {min_temp:.2f}°F")
    print(f"Mean Temperature: {mean_temp:.2f}°F")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_temperatures.py <temperature1> <temperature2> ...")
    else:
        process_temperatures(sys.argv[1:])
