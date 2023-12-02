import streamlit as st
import math

st.title("Statistics Calculator")

choice = st.selectbox("Choose an operation", ["Calculate Mean, Median, and Mode", "Calculate Mean Deviation about the Mean", "Calculate Mean Deviation about the Median", "Calculate Pearson Correlation Coefficient", "Calculate Variance", "Calculate Standard Deviation"])

if choice == "Calculate Mean, Median, and Mode":
    has_frequencies = st.radio("Does the data have frequencies?", ("Yes", "No"))
    
    if has_frequencies == "Yes":
        bins_input = st.text_input("Enter class intervals(e.g:-10,20 20,30 30,40)")
        frequency_input = st.text_input("Enter frequencies(e.g:-1 2 3)")
        
        if bins_input and frequency_input:
            bins = [bin.split(',') for bin in bins_input.split()]
            lower_bounds = [float(bin[0]) for bin in bins]
            upper_bounds = [float(bin[1]) for bin in bins]
            frequencies = [int(x) for x in frequency_input.split()]
            
            midpoints = [(lower + upper) / 2 for lower, upper in zip(lower_bounds, upper_bounds)]
            
            weighted_mean = sum(midpoint * frequency for midpoint, frequency in zip(midpoints, frequencies)) / sum(frequencies)
            weighted_median = statistics.median([midpoint for midpoint, frequency in zip(midpoints, frequencies) for _ in range(frequency)])
            mode = midpoints[frequencies.index(max(frequencies))]  # Mode is the midpoint with the highest frequency
            
            st.write(f"Mean: {weighted_mean}")
            st.write(f"Median: {weighted_median}")
            st.write(f"Mode: {mode}")
    else:
        data_input = st.text_input("Enter data values")
        
        if data_input:
            data = [float(x) for x in data_input.split()]
            
            mean = statistics.mean(data)
            median = statistics.median(data)
            mode = statistics.mode(data)
            
            st.write(f"Mean: {mean}")
            st.write(f"Median: {median}")
            st.write(f"Mode: {mode}")

elif choice == "Calculate Mean Deviation about the Mean":
    class_intervals_input = st.text_input("Enter class intervals (e.g:-10,20 20,30 30,40)")
    frequencies_input = st.text_input("Enter frequencies (e.g:-1 2 3)")

    if class_intervals_input and frequencies_input:
        class_intervals = [tuple(map(int, interval.split(','))) for interval in class_intervals_input.split()]
        frequencies = [int(frequency) for frequency in frequencies_input.split()]

        midpoints = [(lower + upper) / 2 for (lower, upper) in class_intervals]

        total_sum = 0
        n = sum(frequencies)
        for i in range(len(midpoints)):
            total_sum += midpoints[i] * frequencies[i]
        mean = total_sum / n

        mean_deviation = 0
        for i in range(len(midpoints)):
            mean_deviation += abs(midpoints[i] - mean) * frequencies[i]
        mean_deviation /= n

        st.write(f"Mean Deviation about Mean: {mean_deviation:.2f}")

elif choice == "Calculate Mean Deviation about the Median":
    class_intervals_input = st.text_input("Enter class intervals (e.g:-10,20 20,30 30,40)")
    frequencies_input = st.text_input("Enter frequencies (e.g:-1 2 3)")

    if class_intervals_input and frequencies_input:
        class_intervals = [tuple(map(int, interval.split(','))) for interval in class_intervals_input.split()]
        frequencies = [int(frequency) for frequency in frequencies_input.split()]

        midpoints = [(lower + upper) / 2 for (lower, upper) in class_intervals]

        total_sum = sum(frequencies)
        median_index = (total_sum + 1) / 2
        cumulative_freq = 0
        median_class = None
        for i in range(len(class_intervals)):
            cumulative_freq += frequencies[i]
            if cumulative_freq >= median_index:
                median_class = i
                break
        median_lower, median_upper = class_intervals[median_class]
        median = median_lower + ((median_index - (cumulative_freq - frequencies[i])) / frequencies[i]) * (median_upper - median_lower)

        mean_deviation = 0
        for i in range(len(midpoints)):
            mean_deviation += abs(midpoints[i] - median) * frequencies[i]
        mean_deviation /= total_sum

        st.write(f"Mean Deviation about Median: {mean_deviation:.2f}")

elif choice == "Calculate Pearson Correlation Coefficient":
    x_input = st.text_input("Enter values for x (space-separated)")
    y_input = st.text_input("Enter values for y (space-separated)")

    if x_input and y_input:
        x = [int(value) for value in x_input.split(' ')]
        y = [int(value) for value in y_input.split(' ')]
        n = len(x)
        sx, sy = sum(x), sum(y)
        sxy, sxq, syq = 0, 0, 0
        for i in range(n):
            sxy += x[i] * y[i]
            sxq += x[i] ** 2
            syq += y[i] ** 2
        a = (n * sxy) - (sx * sy)
        b = (n * sxq) - (sx ** 2)
        c = (n * syq) - (sy ** 2)
        r = a / ((b**0.5) * (c**0.5))

        st.write("Pearson Correlation Coefficient (r):", round(r, 3))

elif choice == "Calculate Variance":
    intervals_input = st.text_input("Enter class intervals(e.g:-10,20 20,30 30,40)")
    frequencies_input = st.text_input("Enter frequencies(e.g:-1 2 3)")

    if intervals_input and frequencies_input:
        class_intervals = [tuple(map(float, interval.split(','))) for interval in intervals_input.split()]
        frequencies = [int(frequency) for frequency in frequencies_input.split()]

        midpoints = [(lower + upper) / 2 for lower, upper in class_intervals]

        total_sum = sum(midpoints[i] * frequencies[i] for i in range(len(class_intervals)))
        total_frequency = sum(frequencies)
        mean = total_sum / total_frequency
        variance = sum((midpoints[i] - mean) ** 2 * frequencies[i] for i in range(len(class_intervals))) / total_frequency

        st.write(f"Variance: {variance}")

elif choice == "Calculate Standard Deviation":
    intervals_input = st.text_input("Enter class intervals(e.g:-10,20 20,30 30,40)")
    frequencies_input = st.text_input("Enter frequencies(e.g:-1 2 3)")

    if intervals_input and frequencies_input:
        class_intervals = [tuple(map(float, interval.split(','))) for interval in intervals_input.split()]
        frequencies = [int(frequency) for frequency in frequencies_input.split()]

        midpoints = [(lower + upper) / 2 for lower, upper in class_intervals]

        total_sum = sum(midpoints[i] * frequencies[i] for i in range(len(class_intervals)))
        total_frequency = sum(frequencies)
        mean = total_sum / total_frequency
        variance = sum((midpoints[i] - mean) ** 2 * frequencies[i] for i in range(len(class_intervals))) / total_frequency
        standard_deviation = math.sqrt(variance)

        st.write(f"Standard Deviation: {standard_deviation:.2f}")
