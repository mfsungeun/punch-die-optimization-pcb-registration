from odbAccess import * 

import os
import csv

# set working directory
setPath = 'C:/temp/v6'
os.chdir(setPath)
csv_file_path = setPath + '/data/lhs_samples.csv'
error_log_path = setPath + '/data/samples_with_errors.csv'

outputDir = os.path.join(setPath, 'output')
os.makedirs(outputDir, exist_ok=True)


def SaveResultsToCSV(i, punch_clearance, punch_speed, material_thickness):   
    i += 1
    i_padded = str(i).zfill(3)
    clearance_str = f"Clr{punch_clearance:.4f}".replace('.', 'p')  # p=decimal point
    speed_str = f"Spd{punch_speed:.1f}".replace('-', 'm').replace('.', 'p')  # m=minus
    thickness_str = f"Thk{material_thickness:.3f}".replace('.', 'p')
    job_name = f"{i_padded}_Sim_{clearance_str}_{speed_str}_{thickness_str}"
    
    filename = job_name + '.odb'
    filepath = os.path.join(setPath, filename)
    filesize = os.path.getsize(filepath) / 1024 # in KB
    
    if filesize < 100 :
        with open(error_log_path, 'a') as file:
            file.write(f'{filename}, {filesize}\n')
        return i
        
    odb = openOdb(path=filename, readOnly=False)

    step = odb.steps['Punch']
    frame = step.frames[-1] # last frame
    instance = odb.rootAssembly.instances['MATERIAL-1']

    # get stress data
    stress_field = frame.fieldOutputs['S']
    stress_subfield = stress_field.getSubset(region=instance, position=INTEGRATION_POINT, elementType='C3D8R')
    stress_output_file = os.path.join(outputDir, 'S_' + job_name + '.csv')

    with open(stress_output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Element Label', 'S11', 'S22', 'S33', 'S12', 'S13', 'S23','Mises'])
        for value in stress_subfield.values:
            writer.writerow([value.elementLabel] + list(value.data) + [value.mises]) 

    # get coordinates
    coord_field = frame.fieldOutputs['COORD']
    coord_output_file = os.path.join(outputDir, 'COORD_' + job_name + '.csv')

    with open(coord_output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Element Label', 'Node Label', 'x', 'y', 'z'])
        for value in coord_field.values:
            writer.writerow([value.elementLabel] + [value.nodeLabel] + list(value.data))  
            # x=value.data[0], y=value.data[1], z=value.data[2]

    odb.close()
    print(f'{i_padded} {job_name} Saved.')
    return i


i = 0
line_number = 0
start_line = 0 # missing 37, 65, 71, 93, 117
# i = i + start_line

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if line_number < start_line:
            line_number += 1
            continue 
        punch_clearance = float(row['punch_clearance'])
        punch_speed = float(row['punch_speed'])
        material_thickness = float(row['material_thickness'])
        i = SaveResultsToCSV(i, punch_clearance, punch_speed, material_thickness)
        
        