

# Punch and Die Optimization in PCB Registration
This repository contains code and data for optimizing punch and die design to minimize punched deviations in PCB registraion.

<br />

## 🌱 Introduction
This project was completed by Agnes Song and John O'Connor as part of the MFGE/SE 5702 - Data Science in Materials and Manufacturing course in UCONN Master's program. The course focused on ML techniques in manufacturing and materials. The project applies the concepts and skills learned throughout the course.

<br />

## 📍 Objective
This project aims to optimize three parameters (clearance, speed, and thickness) to minimize the punch deviation for the punch and die process in PCB manufacturing. The process involves creating a simulation model in Abaqus, translating it to Python, running output analysis, developing a surrogate model, and running optimization to find the optimal parameter set.

<br />

## 🛠️ Methodology / Development
1. **Simulation Model Development**: We crafted a simulation model in Abaqus to mimic the physical punching process.

    ![image](https://github.com/mfsungeun/punch-die-optimization-pcb-registration/assets/99304990/2811a698-e293-4d51-bc1a-83df2300877e) 
    ![image](https://github.com/mfsungeun/punch-die-optimization-pcb-registration/assets/99304990/943798e5-8b40-44e0-bb70-4325aa3b9e84)

    _Punch simulation assembly (left) and deformed substrate (right)._

2. **Data Generation**: We generated a dataset spanning the defined parameter space using Latin Hypercube Sampling.

    | Design Variable              | Low Value | High Value |
    |------------------------------|-----------|------------|
    | Punch and Die Clearance (in.)| 0.000     | 0.010      |
    | Punch Speed (ft./s)          | -2.0      | -0.1       |
    | Substrate Thickness (in.)    | 0.001     | 0.015      |

3. **Stress Analysis and Response Calculation**: After running simulations, we analyzed stress outputs and coordinates data to calculate response variables.

    ![image](https://github.com/mfsungeun/punch-die-optimization-pcb-registration/assets/99304990/c9db891c-3925-4799-a465-7767af87dd49)

    _Sample mises stress distribution plot_

4. **Surrogate Model Development**: We developed surrogate model by employing various techniques - RBF, Kriging, Random Forest, Neural Network.

5. **Optimization**: We applied Bayesian Optimization and Gradient-based methods to find the optimal parameters.

<br />

## 📁 Project Structure
```
.
│   README.md
│   LICENSE
├── scripts
│   │   00_generate_samples.ipynb
│   │   01_run_simulation.py
│   │   02_save_output.py
│   │   03_output_analysis.ipynb
│   │   04_surrogate_modeling.ipynb
│   │   05_optimization.ipynb
├── data
│   │   lhs_samples.csv
│   │   responses.csv
│   │   samples_with_errors.csv
|   ├── output
```


Scripts:
- 00_generate_samples.ipynb - generate 500 sample data points for simulation.
- 01_run_simulation.py - Python script to run the simulation. Needs to be opened in Abaqus 2023.
- 02_save_output.py - Python script to save the simulation output. Needs to be opened in Abaqus 2023.
- 03_output_analysis.ipynb - analyze the simulation output.
- 04_surrogate_modeling.ipynb - develop surrogate models based on simulation data.
- 05_optimization.ipynb - run optimization algorithms to find optimal parameters.

Data:
- lhs_samples.csv - sample points generated by Latin Hypercube Sampling
- samples_with_errors.csv - samples that had errors during Abaqus simulation, could not be included in analysis
- responses.csv - response data calculated from output analysis
- output - Directory containing raw coordinates and stress output data from Abaqus simulation.
  - `COORD_001_....csv`, `COORD_002...csv`, ..., `COORD_500...csv`: raw coordinate data files.
  - `S_001...csv`, `S_002....csv`, ..., `S_500....csv`: stress output data files.

<br />

## 📊 Results
- Our analysis revealed mild positive correlation in punch clearance and negative correlations in substrate thickness.
- Surrogate models showed promise but need refinement for better predictive accuracy. Random Forest and Neural Network emerged as the most effective surrogate models.
- Gradient-based and Bayesian optimization techniques converged on similar parameter sets.

<br />

## 💭 Future Improvements
Future improvements on this project would include:
- generating high-fidelity dataset to validate optimization results
- enhance simulation accuracy by increasing mesh size
- refining response calculations

