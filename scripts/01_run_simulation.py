# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

import os
import csv

# set working directory
setPath = 'C:/temp/v6'
os.chdir(setPath)
csv_file_path = setPath + '/scripts/lhs_samples.csv'

        
def RunSimulation(i, punch_clearance, punch_speed, material_thickness):
    i += 1
    i_padded = str(i).zfill(3)
    clearance_str = f"Clr{punch_clearance:.4f}".replace('.', 'p')  # p=decimal point
    speed_str = f"Spd{punch_speed:.1f}".replace('-', 'm').replace('.', 'p')  # m=minus
    thickness_str = f"Thk{material_thickness:.3f}".replace('.', 'p')
    job_name = f"{i_padded}_Sim_{clearance_str}_{speed_str}_{thickness_str}"
    # job_name = f"Sim_Clr{punch_clearance:.4f}_Spd{punch_speed:.1f}_Thk{material_thickness:.3f}"
        
    
    model_name = 'Model_' + i_padded
    # job_name = 'Sim_' + str(i) 
    # job_name = "Punch_" + str(i) + "_" + clearance_str[-3:-1] + "_" + matl_str[-3:-1]
    # output_csv_path = './' + str(i) +'_stress_output.csv'
    # output_csv_path = './output/' + parameter_type + '_' + str(i) +'_stress_output.csv'
    
    m = mdb.Model(name=model_name) # create model
    
    m.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[0])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(11.25, 16.25))
    del m.sketches['__profile__']
    m.ConstrainedSketch(name='__profile__', sheetSize=2.0)
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[0])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.275, 0.125))
    m.sketches['__profile__'].setAsConstruction(objectList=(m.sketches['__profile__'].geometry[2], ))
    m.sketches['__profile__'].rectangle(point1=(-0.2375,0.186664806538349), point2=(0.125, -0.275))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[3], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[5], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[6], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.373333334922791, 0.0130893886089325), value=0.25, 
        vertex1=m.sketches['__profile__'].vertices[3], 
        vertex2=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(0.0193495750427246, 0.187235742807388), value=0.1875, 
        vertex1=m.sketches['__profile__'].vertices[6], 
        vertex2=m.sketches['__profile__'].vertices[3])
    m.sketches['__profile__'].Parameter(
        expression=str(punch_clearance), name='Punch_Clearance')
    m.sketches['__profile__'].Parameter(
        expression='0.1875 - (2*Punch_Clearance)', name='Punch_Width', 
        path='dimensions[1]', previousParameter='Punch_Clearance')
    m.sketches['__profile__'].Parameter(
        expression='0.25 - (2*Punch_Clearance)', name='Punch_Height', 
        path='dimensions[0]', previousParameter='Punch_Width')
    m.Part(dimensionality=THREE_D, name='Punch', type=DEFORMABLE_BODY)
    m.parts['Punch'].BaseSolidExtrude(depth=1.25, sketch=m.sketches['__profile__'])
    del m.sketches['__profile__']
    m.ConstrainedSketch(name='__profile__', sheetSize=2.0)
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[0])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.3, 0.1625))
    m.sketches['__profile__'].RadialDimension(
        curve=m.sketches['__profile__'].geometry[2], radius=0.5, 
        textPoint=(-0.547479689121246, 0.0529268085956573))
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.15, 0.1))
    m.sketches['__profile__'].setAsConstruction(objectList=(m.sketches['__profile__'].geometry[3], ))
    m.sketches['__profile__'].rectangle(point1=(-0.1125, 0.14086784586981), point2=(0.05, -0.173205080756887))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[5], 
        entity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[7], 
        entity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[8], 
        entity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.253821134567261, 0.0210568904876709), value=0.25, 
        vertex1=m.sketches['__profile__'].vertices[5], 
        vertex2=m.sketches['__profile__'].vertices[6])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(0.00227642059326172, 0.216829270124435), value=0.1875, 
        vertex1=m.sketches['__profile__'].vertices[8], 
        vertex2=m.sketches['__profile__'].vertices[5])
    m.sketches['__profile__'].Parameter(
        expression=str(punch_clearance), name='Guide_Clearance')
    m.sketches['__profile__'].Parameter(
        expression='0.1875 - (2*Guide_Clearance) + 0.001', name='Guide_Width', 
        path='dimensions[2]', previousParameter='Guide_Clearance')
    m.sketches['__profile__'].Parameter(
        expression='0.25 - (2*Guide_Clearance) + 0.001', name='Guide_Length', 
        path='dimensions[1]', previousParameter='Guide_Width')
    m.Part(dimensionality=THREE_D, name='Guide', type=DEFORMABLE_BODY)
    m.parts['Guide'].BaseSolidExtrude(depth=1.0, sketch=m.sketches['__profile__'])
    del m.sketches['__profile__']
    m.ConstrainedSketch(name='__profile__', sheetSize=2.0)
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[0])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.35, 0.1875))
    m.sketches['__profile__'].RadialDimension(curve=m.sketches['__profile__'].geometry[2], radius=0.5, 
        textPoint=(-0.530406475067139, 0.0438210964202881))
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.1375, 0.1125))
    m.sketches['__profile__'].rectangle(point1=(-0.1125, 0.1375), point2=(0.0625, -0.166301683695625))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[5], 
        entity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[7], 
        entity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].setAsConstruction(objectList=(m.sketches['__profile__'].geometry[3], ))
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[8], e
        ntity2=m.sketches['__profile__'].geometry[3])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.227642178535461, 0.011951208114624), value=0.25, 
        vertex1=m.sketches['__profile__'].vertices[5], 
        vertex2=m.sketches['__profile__'].vertices[6])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.00796741247177124, 0.22593492269516), value=0.1875, 
        vertex1=m.sketches['__profile__'].vertices[8], 
        vertex2=m.sketches['__profile__'].vertices[5])
    m.sketches['__profile__'].Parameter(
        expression='0.1875', name='Die_Width', path='dimensions[2]')
    m.sketches['__profile__'].Parameter(
        expression='0.25', name='Guide_Length', 
        path='dimensions[1]', previousParameter='Die_Width')
    m.Part(dimensionality=THREE_D, name='Die', type=DEFORMABLE_BODY)
    m.parts['Die'].BaseSolidExtrude(depth=1.0, sketch=m.sketches['__profile__'])
    del m.sketches['__profile__']
    m.ConstrainedSketch(name='__profile__', sheetSize=2.0)
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[0])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.125, 0.1375))
    m.sketches['__profile__'].setAsConstruction(objectList=(m.sketches['__profile__'].geometry[2], ))
    m.sketches['__profile__'].rectangle(point1=(-0.117247919444554, 0.144167178601523), point2=(0.0625, -0.175))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[3], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[5], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[6], 
        entity2=m.sketches['__profile__'].geometry[2])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.277723520994186, 0.0313007831573486), value=1.0, 
        vertex1=m.sketches['__profile__'].vertices[3], 
        vertex2=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.00866313651204109, 0.543268859386444), value=0.032, 
        vertex1=m.sketches['__profile__'].vertices[6], 
        vertex2=m.sketches['__profile__'].vertices[3])
    m.sketches['__profile__'].Parameter(expression=str(material_thickness), 
        name='Material_Thickness', path='dimensions[1]')
    m.Part(dimensionality=THREE_D, name='Material', type=DEFORMABLE_BODY)
    m.parts['Material'].BaseSolidExtrude(depth=1.0, sketch=m.sketches['__profile__'])
    del m.sketches['__profile__']
    
    m.Material(name='Aluminum')
    m.materials['Aluminum'].DuctileDamageInitiation(table=((1.5018, 0.133, 250.0), ))
    m.materials['Aluminum'].Density(table=((0.0975, ), ))
    m.materials['Aluminum'].Elastic(table=((10000000.0, 0.33), ))
    m.materials['Aluminum'].Plastic(scaleStress=None, table=((40000.0, 0.0), ))
    
    m.Material(name='A2 Tool Steel')
    m.materials['A2 Tool Steel'].Density(table=((0.284, ), ))
    m.materials['A2 Tool Steel'].Elastic(table=((29400000.0, 0.3), ))
    
    m.HomogeneousSolidSection(material='Aluminum', name='Aluminum', thickness=None)
    m.parts['Material'].Set(
        cells=m.parts['Material'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-1')
    m.parts['Material'].SectionAssignment(
        offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
        region=m.parts['Material'].sets['Set-1'], 
        sectionName='Aluminum', thicknessAssignment=FROM_SECTION)
        
    m.HomogeneousSolidSection(
        material='A2 Tool Steel', name='A2 Tool Steel', thickness=None)
    m.parts['Punch'].Set(
        cells=m.parts['Punch'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-1')
    m.parts['Punch'].SectionAssignment(
        offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
        region=m.parts['Punch'].sets['Set-1'], sectionName='A2 Tool Steel', thicknessAssignment=FROM_SECTION)
    m.parts['Guide'].Set(
        cells=m.parts['Guide'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-1')
    m.parts['Guide'].SectionAssignment(
        offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
        region=m.parts['Guide'].sets['Set-1'], sectionName='A2 Tool Steel', thicknessAssignment=FROM_SECTION)
    m.parts['Die'].Set(
        cells=m.parts['Die'].cells.getSequenceFromMask(('[#1 ]', ), ), name='Set-1')
    m.parts['Die'].SectionAssignment(
        offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
        region=m.parts['Die'].sets['Set-1'], sectionName='A2 Tool Steel', thicknessAssignment=FROM_SECTION)
        
    m.rootAssembly.DatumCsysByDefault(CARTESIAN)
    m.rootAssembly.Instance(dependent=ON, name='Punch-1', part=m.parts['Punch'])
    m.rootAssembly.Instance(dependent=ON, name='Die-1', part=m.parts['Die'])
    m.rootAssembly.Instance(dependent=ON, name='Material-1', part=m.parts['Material'])
    m.rootAssembly.translate(instanceList=('Die-1', ), vector=(0.0, 0.0, -1.25))
    m.rootAssembly.translate(instanceList=('Material-1', ), vector=(0.0, 0.0, -1.0))
    m.rootAssembly.rotate(angle=90.0, 
        axisDirection=(0.0, -2.0, 0.0), axisPoint=(0.0, 1.0, 0.0), 
        instanceList=('Material-1', ))
    m.rootAssembly.translate(instanceList=('Material-1', ), vector=(-0.5, 0.0, 0.0))
    m.rootAssembly.translate(instanceList=('Die-1', ), vector=(0.0, 0.0, 0.25))
    m.rootAssembly.translate(instanceList=('Material-1', ), vector=(0.0, 0.0, 0.032))
    m.rootAssembly.Instance(dependent=ON, name='Guide-1', part=m.parts['Guide'])
    m.rootAssembly.translate(instanceList=('Guide-1', ), vector=(0.0, 0.0, 0.125))
    m.rootAssembly.translate(instanceList=('Punch-1', ), vector=(0.0, 0.0, 0.125))
    m.ExplicitDynamicsStep(improvedDtMethod=ON, name='Punch', 
        previous='Initial', timePeriod=0.08) #STEP TIME
        
    m.ContactProperty('Frictionless')
    m.interactionProperties['Frictionless'].TangentialBehavior(formulation=FRICTIONLESS)
    
    m.ContactProperty('Friction')
    m.interactionProperties['Friction'].TangentialBehavior(
        elasticSlipStiffness=None, exponentialDecayDefinition=COEFFICIENTS, 
        formulation=EXPONENTIAL_DECAY, fraction=0.005, maximumElasticSlip=FRACTION, 
        table=((0.61, 0.471, 1.0), ))
        
    m.ContactProperty('Damage')
    m.interactionProperties['Damage'].TangentialBehavior(
        elasticSlipStiffness=None, exponentialDecayDefinition=COEFFICIENTS, 
        formulation=EXPONENTIAL_DECAY, fraction=0.005, maximumElasticSlip=FRACTION, 
        table=((0.61, 0.47, 1.0), ))
    m.interactionProperties['Damage'].NormalBehavior(
        allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
        pressureOverclosure=HARD)
        
    m.rootAssembly.Surface(name='m_Surf-1', side1Faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#2 ]', ), ))
    m.rootAssembly.Surface(name='Punch_1', side1Faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#4 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Frictionless', 
        main=m.rootAssembly.surfaces['m_Surf-1'], mechanicalConstraint=KINEMATIC, name='Punch_Guide_1', 
        secondary=m.rootAssembly.surfaces['Punch_1'], sliding=FINITE)
    m.rootAssembly.Surface(name='Guide_2', side1Faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#8 ]', ), ))
    m.rootAssembly.Surface(name='Punch_2', side1Faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#1 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Frictionless', 
        main=m.rootAssembly.surfaces['Guide_2'], 
        mechanicalConstraint=KINEMATIC, name='Punch_Guide_2', 
        secondary=m.rootAssembly.surfaces['Punch_2'], sliding=FINITE)
    m.rootAssembly.Surface(name='Guide_3', side1Faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#4 ]', ), ))
    m.rootAssembly.Surface(name='Punch_3', side1Faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#2 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Frictionless', 
        main=m.rootAssembly.surfaces['Guide_3'], 
        mechanicalConstraint=KINEMATIC, name='Punch_Guide_3', 
        secondary=m.rootAssembly.surfaces['Punch_3'], sliding=FINITE)
    m.rootAssembly.Surface(name='Guide_4', side1Faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#10 ]', ), ))
    m.rootAssembly.Surface(name='Punch_4', side1Faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#8 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Friction', 
        main=m.rootAssembly.surfaces['Guide_4'], 
        mechanicalConstraint=KINEMATIC, name='Punch_Guide_4', 
        secondary=m.rootAssembly.surfaces['Punch_4'], sliding=FINITE)
    m.interactions['Punch_Guide_4'].setValues(clearanceRegion=None, 
        datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Frictionless', mechanicalConstraint=KINEMATIC, sliding=FINITE)
    m.rootAssembly.Surface(name='Guide_5', side1Faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#40 ]', ), ))
    m.rootAssembly.Surface(name='Material_1', side1Faces=
        m.rootAssembly.instances['Material-1'].faces.getSequenceFromMask(('[#1 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Frictionless', 
        main=m.rootAssembly.surfaces['Guide_5'], 
        mechanicalConstraint=KINEMATIC, name='Guide_Material', 
        secondary=m.rootAssembly.surfaces['Material_1'], sliding=FINITE)
    m.interactions['Guide_Material'].setValues(clearanceRegion=
        None, datumAxis=None, initialClearance=OMIT, interactionProperty='Damage', 
        mechanicalConstraint=KINEMATIC, sliding=FINITE)
    m.rootAssembly.Surface(name='Die_1', side1Faces=
        m.rootAssembly.instances['Die-1'].faces.getSequenceFromMask(('[#20 ]', ), ))
    m.rootAssembly.Surface(name='Material_2', side1Faces=
        m.rootAssembly.instances['Material-1'].faces.getSequenceFromMask(('[#4 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Damage', 
        main=m.rootAssembly.surfaces['Die_1'], mechanicalConstraint=
        KINEMATIC, name='Die_Material_1', 
        secondary=m.rootAssembly.surfaces['Material_2'], sliding=FINITE)
    m.rootAssembly.Surface(name='Punch_5', side1Faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#20 ]', ), ))
    m.SurfaceToSurfaceContactExp(clearanceRegion=None, 
        createStepName='Initial', datumAxis=None, initialClearance=OMIT, 
        interactionProperty='Damage', 
        main=m.rootAssembly.surfaces['Punch_5'], 
        mechanicalConstraint=KINEMATIC, name='Punch_Material_1', 
        secondary=Region(side1Faces=m.rootAssembly.instances['Material-1'].faces.getSequenceFromMask(
        mask=('[#1 ]', ), )), sliding=FINITE)
        
    m.SurfaceTraction(createStepName='Punch', directionVector=(
        (0.0, 0.0, 0.0), (0.0, 0.0, -1.0)), distributionType=UNIFORM, field='', 
        localCsys=None, magnitude=1500.0, name='Punch', region=Region(
        side1Faces=m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(
        mask=('[#10 ]', ), )), traction=GENERAL)
    m.SurfaceTraction(createStepName='Punch', directionVector=(
        (0.0, 0.0, 0.0), (0.0, 0.0, -1.0)), distributionType=UNIFORM, field='', 
        localCsys=None, magnitude=45, name='Guide', region=Region(
        side1Faces=m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(
        mask=('[#20 ]', ), )), traction=GENERAL)
        
    m.rootAssembly.Set(faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-1')
    m.DisplacementBC(amplitude=UNSET, createStepName='Punch', 
        distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='Punch', 
        region=m.rootAssembly.sets['Set-1'], u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0)
    m.rootAssembly.Set(faces=
        m.rootAssembly.instances['Guide-1'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-2')
    m.DisplacementBC(amplitude=UNSET, createStepName='Punch', 
        distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='Guide', 
        region=m.rootAssembly.sets['Set-2'], u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0)
    m.rootAssembly.Set(faces=
        m.rootAssembly.instances['Die-1'].faces.getSequenceFromMask(('[#1 ]', ), ), name='Set-3')
    m.DisplacementBC(amplitude=UNSET, createStepName='Punch', 
        distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='Die', 
        region=m.rootAssembly.sets['Set-3'], u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0)
    
    m.parts['Punch'].seedPart(deviationFactor=0.25, minSizeFactor=0.1, size=1.0) #0.08
    m.parts['Punch'].generateMesh()
            
    m.parts['Material'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=0.5) #Altered mesh 0.06
    m.parts['Material'].generateMesh()
    
    m.parts['Die'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=1.0) #0.25
    m.parts['Die'].generateMesh()
    
    m.parts['Guide'].seedPart(deviationFactor=0.1, minSizeFactor=0.1, size=0.5) #0.35
    m.parts['Guide'].generateMesh()
    m.rootAssembly.regenerate()
    
    
    del m.materials['Aluminum'].ductileDamageInitiation
    del m.materials['Aluminum'].plastic
    m.materials['Aluminum'].DuctileDamageInitiation(table=((0.07, 0, 0), ))
    m.materials['Aluminum'].Plastic(scaleStress=None, table=((
        2541.060542, 0.0), (2947.261406, 0.00010539), (3368.157626, 0.000135243), (
        3796.891555, 0.000171397), (4232.896333, 0.000206957), (4672.658377, 
        0.000241683), (5118.267095, 0.000279895), (5570.544087, 0.000317705), (
        6025.911603, 0.000360846), (6483.429732, 0.000402296), (6944.360584, 
        0.000444131), (7412.61518, 0.000490696), (7887.746125, 0.00053841), (
        8363.021915, 0.000586271), (8842.049202, 0.000637285), (9324.07129, 
        0.000683704), (9811.527923, 0.000730495), (10299.72805, 0.000778863), (
        10786.58262, 0.000823852), (11274.62321, 0.000873199), (11763.86927, 
        0.000925883), (12247.55196, 0.00097877), (12730.45955, 0.001029195), (
        13212.003, 0.001082), (13694.99398, 0.001130606), (14178.32661, 
        0.001180995), (14653.25242, 0.001231786), (15127.8778, 0.00128302), (
        15606.70211, 0.001332034), (16085.33628, 0.001386209), (16560.26365, 
        0.001439068), (17033.00074, 0.001487205), (17504.07249, 0.001538396), (
        17977.20237, 0.001591006), (18451.14682, 0.001639952), (18920.97058, 
        0.001690493), (19384.62637, 0.001740252), (19846.67433, 0.001788971), (
        20306.81772, 0.001845505), (20760.41805, 0.001894663), (21207.4669, 
        0.00194257), (21650.41322, 0.001990877), (22093.09132, 0.002039445), (
        22535.60013, 0.002091081), (22974.89629, 0.002143031), (23408.8999, 
        0.002190634), (23840.47615, 0.002241237), (24275.03522, 0.002293238), (
        24705.71634, 0.002347461), (25128.44602, 0.002400879), (25546.17666, 
        0.002452607), (25962.62719, 0.002501761), (26381.79549, 0.002554876), (
        26795.15511, 0.002606502), (27206.47469, 0.002655511), (27614.14473, 
        0.002705631), (28022.12445, 0.0027538), (28429.20816, 0.002807737), (
        28834.31583, 0.002861748), (29230.96702, 0.002913364), (29629.19666, 
        0.002965219), (30016.67255, 0.003018059), (30403.00649, 0.003071731), (
        30781.4448, 0.003127864), (31158.65134, 0.003181331), (31530.38888, 
        0.003239392), (31893.46129, 0.003297522), (32252.92184, 0.003360121), (
        32608.36677, 0.003424882), (32959.47989, 0.003490619), (33306.73655, 
        0.003562222), (33643.94037, 0.003636113), (33973.34788, 0.003717755), (
        34297.87659, 0.003812926), (34610.62299, 0.003915972), (34914.5646, 
        0.004029277), (35195.6938, 0.004157094), (35457.17556, 0.004296743), (
        35691.58368, 0.004447814), (35895.53939, 0.004607709), (36072.25759, 
        0.004772679), (36215.265, 0.004942059), (36332.51322, 0.005116236), (
        36425.13926, 0.005293914), (36498.52273, 0.005473275), (36558.28435, 
        0.005652689), (36608.17279, 0.005834702), (36649.1646, 0.006017624), (
        36687.13975, 0.006205252), (36716.95295, 0.00639216), (36748.04592, 
        0.006575816), (36773.58345, 0.006760906), (36798.72115, 0.006946395), (
        36820.66399, 0.007134093), (36838.84515, 0.007324967), (36859.71439, 
        0.007514319), (36878.90371, 0.007706937), (36895.49444, 0.007898117), (
        36912.27437, 0.008088437), (36927.2268, 0.008282125), (36944.66887, 
        0.008471925), (36960.50547, 0.008660029), (36973.88299, 0.008846222), (
        36990.51876, 0.009029449), (37005.49193, 0.00921754), (37021.59437, 
        0.00940601), (37033.9345, 0.009592596), (37048.35778, 0.009780054), (
        37066.0277, 0.009967218), (37080.10801, 0.010157017), (37095.6183, 
        0.010346499), (37109.8198, 0.010536207), (37123.91168, 0.010724979), (
        37139.6703, 0.010911731), (37153.33539, 0.011101625), (37167.80224, 
        0.01129417), (37181.21883, 0.011479162), (37192.4888, 0.011667281), (
        37207.44655, 0.011851804), (37221.20893, 0.012036642), (37236.61792, 
        0.012222882), (37249.63943, 0.012404735), (37262.83616, 0.012582674), (
        37278.44948, 0.012767636), (37292.66114, 0.01295317), (37307.02386, 
        0.013137335), (37320.34611, 0.013320279), (37334.33542, 0.013503574), (
        37348.47204, 0.013687487), (37360.12783, 0.01386943), (37373.11058, 
        0.014049965), (37388.77569, 0.014227443), (37402.05188, 0.014408663), (
        37418.24879, 0.014589227), (37433.58923, 0.014768384), (37448.30877, 
        0.014947437), (37462.79524, 0.015126778), (37479.76577, 0.015303796), (
        37492.6354, 0.015484635), (37504.18788, 0.015661663), (37517.3775, 
        0.015839289), (37528.98517, 0.016014028), (37542.22774, 0.016187284), (
        37558.90746, 0.016360802), (37570.13219, 0.016535587), (37584.67254, 
        0.016707441), (37596.8816, 0.016879879), (37609.93575, 0.017052961), (
        37625.09692, 0.017229475), (37636.63982, 0.017405435), (37653.02839, 
        0.017583828), (37667.90988, 0.017761222), (37680.41031, 0.017938015), (
        37697.71167, 0.018116075), (37710.13471, 0.018293691), (37723.86626, 
        0.018468082), (37738.47028, 0.018644086), (37748.13577, 0.018818777), (
        37759.18727, 0.018994763), (37771.98552, 0.019170251), (37786.53459, 
        0.019347722), (37801.37783, 0.01952459), (37812.94561, 0.019699479), (
        37827.57466, 0.019876764), (37841.00411, 0.020050823), (37856.42424, 
        0.020229619), (37870.24402, 0.020402978), (37882.60444, 0.020574854), (
        37896.36533, 0.020747017), (37908.70211, 0.020926106), (37923.56158, 
        0.021100115), (37936.18363, 0.021274917), (37948.01352, 0.021443533), (
        37962.08395, 0.021618327), (37975.06101, 0.021792936), (37985.31768, 
        0.021965704), (38001.53028, 0.022131506), (38013.65578, 0.022304314), (
        38027.69883, 0.022474446), (38042.24101, 0.022648128), (38053.84225, 
        0.022816666), (38064.43714, 0.022984307), (38079.48746, 0.023151892), (
        38091.46576, 0.023325606), (38103.07361, 0.02349124), (38116.05333, 
        0.02366293), (38125.34963, 0.023831249), (38140.84212, 0.024003816), (
        38156.1117, 0.024176629), (38168.11078, 0.02434906), (38182.04294, 
        0.024518789), (38196.40748, 0.024689087), (38207.50213, 0.024855666), (
        38223.14963, 0.025027244), (38233.70469, 0.025200345), (38246.21688, 
        0.025370517), (38260.42238, 0.025540896), (38271.22397, 0.025710726), (
        38283.7676, 0.025884165), (38296.08883, 0.026055806), (38308.36352, 
        0.026221932), (38321.27218, 0.02638699), (38333.14246, 0.026554671), (
        38343.80107, 0.02671878), (38356.49018, 0.026883167), (38371.30928, 
        0.027049381), (38385.20589, 0.02721763), (38398.56587, 0.027388436), (
        38411.64814, 0.027557913), (38425.0011, 0.027724), (38437.99487, 
        0.027893039), (38452.2179, 0.028065546), (38459.24121, 0.028234239), (
        38470.66824, 0.028405628), (38482.52572, 0.02857412), (38493.0985, 
        0.02874213), (38506.14472, 0.028911166), (38518.09634, 0.029080945), (
        38529.81414, 0.029246887), (38544.34393, 0.029413327), (38554.93065, 
        0.029577973), (38564.45496, 0.029742385), (38577.23046, 0.029908677), (
        38588.69109, 0.030077789), (38602.65172, 0.030243134), (38612.46728, 
        0.030410124), (38622.31602, 0.030576344), (38634.47881, 0.030742349), (
        38647.53593, 0.030911462), (38656.69259, 0.031087246), (38668.68797, 
        0.031253673), (38679.67163, 0.031423375), (38691.77707, 0.031592385), (
        38704.70022, 0.031764852), (38717.96506, 0.031934871), (38727.94024, 
        0.032104978), (38741.99087, 0.032267651), (38751.9226, 0.032436517), (
        38762.74617, 0.032606967), (38772.79322, 0.032776498), (38783.655, 
        0.032944179), (38794.98027, 0.033114064), (38806.03412, 0.033281304), (
        38816.31942, 0.033447369), (38825.81497, 0.03361444), (38834.42547, 
        0.033782231), (38846.40424, 0.033952261), (38856.51456, 0.034117908), (
        38866.50106, 0.034285477), (38879.4627, 0.034453872), (38891.33527, 
        0.034623963), (38904.30056, 0.034792369), (38913.99332, 0.034970452), (
        38924.64091, 0.035137148), (38936.03583, 0.035305163), (38943.43487, 
        0.035471454), (38953.72208, 0.035638523), (38961.12038, 0.035803918), (
        38970.34837, 0.035972336), (38982.75257, 0.036129475), (38992.51556, 
        0.036290419), (39001.22848, 0.036455315), (39013.34407, 0.036622032), (
        39023.96217, 0.036786056), (39037.44364, 0.036950742), (39041.33428, 
        0.037117051), (39051.32844, 0.037282386), (39062.89822, 0.037452189), (
        39075.69727, 0.037620997), (39087.91702, 0.037786909), (39096.03664, 
        0.037954468), (39102.76566, 0.038122963), (39117.43099, 0.038290905), (
        39125.85013, 0.038459021), (39132.96879, 0.038628181), (39141.62364, 
        0.038796449), (39151.113, 0.038963352), (39162.44805, 0.039133139), (
        39174.726, 0.039305055), (39185.49492, 0.039474304), (39196.1797, 
        0.039643505), (39208.01828, 0.039814491), (39218.1273, 0.03998548), (
        39227.56462, 0.040156548), (39235.92566, 0.04032713), (39241.28076, 
        0.040493501), (39252.69081, 0.040665886), (39261.50799, 0.040840354), (
        39268.95094, 0.041008327), (39277.25201, 0.041176645), (39284.942, 
        0.041347979), (39295.38505, 0.041515822), (39306.45449, 0.041687111), (
        39313.65215, 0.041854919), (39323.30214, 0.042020453), (39332.50788, 
        0.042189687), (39341.06403, 0.042358626), (39350.38189, 0.04252542), (
        39356.72931, 0.042694259), (39365.81407, 0.042863794), (39370.57597, 
        0.043029454), (39379.47369, 0.043196102), (39389.73832, 0.043362935), (
        39398.21916, 0.043532067), (39405.97768, 0.043699257), (39411.04334, 
        0.043866844), (39418.60484, 0.044031442), (39430.71452, 0.044197103), (
        39437.27083, 0.044365268), (39442.77824, 0.044531015), (39449.12005, 
        0.044695701), (39456.75435, 0.044864778), (39468.88229, 0.04503279), (
        39476.83722, 0.045202131), (39486.59263, 0.045370662), (39494.96507, 
        0.045542145), (39504.41106, 0.045711533), (39514.89662, 0.045883234), (
        39520.57685, 0.046054543), (39527.686, 0.046226011), (39536.91219, 
        0.046396075), (39543.07659, 0.046568266), (39550.87633, 0.046735001), (
        39558.0177, 0.046907755), (39565.96517, 0.04707862), (39576.78089, 
        0.047248646), (39583.91008, 0.047418551), (39590.13229, 0.047589914), (
        39596.47313, 0.047761376), (39604.44071, 0.047934016), (39609.90599, 
        0.0481083), (39615.75874, 0.048277793), (39624.04916, 0.048450139), (
        39633.09051, 0.048621414), (39641.07513, 0.048792044), (39646.45749, 
        0.04896111), (39652.27795, 0.049132353), (39660.29551, 0.04930131), (
        39665.84082, 0.049474119), (39669.61946, 0.049644586), (39672.22723, 
        0.049815567), (39675.5322, 0.049985307), (39685.93956, 0.050157175), (
        39693.66594, 0.050327029), (39700.22897, 0.050497248), (39702.50382, 
        0.050666592), (39710.26722, 0.050837017), (39722.59494, 0.051007367), (
        39729.86489, 0.051179256), (39734.82012, 0.051354245), (39741.21053, 
        0.051526212), (39746.25074, 0.051698624), (39757.38448, 0.051871186), (
        39762.36082, 0.052043628), (39764.84371, 0.052219459), (39772.24755, 
        0.052394888), (39777.05349, 0.05256344), (39783.08019, 0.052737254), (
        39788.57415, 0.052907769), (39795.60122, 0.053079634), (39802.10747, 
        0.053249758), (39806.13323, 0.053417726), (39812.4087, 0.053585162), (
        39815.74448, 0.053754586), (39819.30192, 0.053921996), (39827.47284, 
        0.054095441), (39832.0957, 0.054266954), (39835.75067, 0.054438679), (
        39841.99098, 0.054612091), (39848.30451, 0.054788744), (39858.07725, 
        0.054966816), (39863.47876, 0.055144742), (39867.28535, 0.055320631), (
        39872.65256, 0.055496864), (39879.54125, 0.055674767), (39885.28581, 
        0.055853275), (39889.54409, 0.056027428), (39893.49143, 0.056200987), (
        39899.30848, 0.056374071), (39905.36529, 0.056548119), (39906.12707, 
        0.056721157), (39908.33402, 0.056891457), (39915.12632, 0.057062194), (
        39919.24147, 0.057235835), (39922.12069, 0.057412145), (39924.81334, 
        0.057587342), (39929.65394, 0.057761054), (39938.76409, 0.057937741), (
        39945.48205, 0.058116411), (39949.31321, 0.058292333), (39953.22434, 
        0.058465818), (39957.91142, 0.058641849), (39966.00011, 0.058817704), (
        39969.3733, 0.058993491), (39972.97658, 0.059169514), (39977.52763, 
        0.059345063), (39980.11275, 0.059520582), (39985.57853, 0.059699021), (
        39988.74368, 0.059874425), (39991.26999, 0.060054585), (39994.23046, 
        0.060235283), (39996.656, 0.060410376), (40001.17208, 0.060587665), (
        40006.25113, 0.060764238), (40009.46315, 0.060939409), (40016.37469, 
        0.061114558), (40019.76901, 0.061287494), (40026.92113, 0.061459809), (
        40028.11874, 0.061636448), (40030.23437, 0.061812781), (40035.82892, 
        0.061990733), (40039.03869, 0.062169899), (40041.00409, 0.062346829), (
        40043.83954, 0.062524503), (40045.06808, 0.062703844), (40054.04454, 
        0.062881277), (40058.47819, 0.06305319), (40060.94457, 0.063227565), (
        40063.34211, 0.063401192), (40066.12294, 0.06357845), (40067.66962, 
        0.063752219), (40068.69376, 0.063927177), (40072.94121, 0.064102562), (
        40078.23668, 0.064281944), (40080.31631, 0.064461799), (40083.31452, 
        0.06463984), (40087.76213, 0.064816806), (40094.78344, 0.06499611), (
        40101.50351, 0.065173608), (40102.94326, 0.065352499), (40104.4807, 
        0.065533569), (40106.09661, 0.065711504), (40112.58536, 0.06589456), (
        40114.85762, 0.066076272), (40115.64156, 0.066256391), (40116.94012, 
        0.066438891), (40118.96011, 0.066620477), (40122.31816, 0.066803235), (
        40124.96951, 0.066987591), (40125.37347, 0.067172092), (40128.58211, 
        0.067353582), (40130.0873, 0.067536407), (40132.56148, 0.067718372), (
        40136.02286, 0.067900307), (40134.59172, 0.068081388), (40135.66413, 
        0.068260613), (40138.12592, 0.068438057), (40139.37755, 0.068618176), (
        40142.63535, 0.068801458), (40142.45017, 0.06897765), (40145.06117, 
        0.069156974), (40148.68205, 0.069338416), (40152.80214, 0.069522036), (
        40150.72193, 0.069705161), (40150.19052, 0.069889646), (40154.67839, 
        0.070067983), (40160.41483, 0.070254299), (40160.01687, 0.070438396), (
        40162.21669, 0.070620136), (40163.64557, 0.070798404), (40166.89928, 
        0.070978788), (40170.06058, 0.071158662), (40169.70813, 0.071343044), (
        40168.78941, 0.071526811), (40166.21772, 0.071711403), (40167.59168, 
        0.071896633), (40169.73595, 0.072084298), (40172.68847, 0.072271166), (
        40174.55339, 0.072456703), (40176.44261, 0.072640265), (40177.97807, 
        0.072825128), (40181.15019, 0.073007816), (40179.60015, 0.073189827), (
        40178.67624, 0.073371098), (40178.25235, 0.073553502), (40178.1432, 
        0.073737474), (40176.9313, 0.073923883), (40177.74277, 0.07410826), (
        40181.18617, 0.074297697), (40183.63309, 0.07448466), (40185.46969, 
        0.074676036), (40185.70325, 0.07486438), (40187.26236, 0.075052541), (
        40186.78248, 0.075237943), (40185.38101, 0.075424159), (40183.85127, 
        0.075611114), (40182.98156, 0.075797178), (40178.93623, 0.075982602), (
        40180.62214, 0.076170392), (40177.80654, 0.076359872), (40175.19221, 
        0.076550791), (40173.63597, 0.076741611), (40172.66661, 0.076931307), (
        40173.18819, 0.077122668), (40172.31854, 0.077312463), (40170.08766, 
        0.077500126), (40168.88392, 0.077688395), (40167.77814, 0.077880119), (
        40162.02302, 0.078072822), (40154.60739, 0.078259737), (40149.13952, 
        0.078449808), (40147.62963, 0.078636717), (40141.19088, 0.078829014), (
        40135.76966, 0.079019303), (40126.49943, 0.079208723), (40123.23064, 
        0.079398303), (40119.74648, 0.079592276), (40111.74704, 0.079783908), (
        40101.133, 0.079980445), (40090.05918, 0.080173421), (40077.95363, 
        0.080368376), (40068.78414, 0.080566132), (40054.25316, 0.080759199), (
        40037.49533, 0.080953722), (40019.69464, 0.081150827)))
    m.materials['Aluminum'].ductileDamageInitiation.DamageEvolution(table=((0.035086, ), ), type=DISPLACEMENT)
    m.rootAssembly.Set(faces=
        m.rootAssembly.instances['Punch-1'].faces.getSequenceFromMask(('[#10 ]', ), ), name='Set-4')
           
    m.VelocityBC(amplitude=UNSET, createStepName='Punch',distributionType=UNIFORM, 
        fieldName='', localCsys=None, name='BC-4',region=m.rootAssembly.sets['Set-4'], 
        v1=UNSET, v2=UNSET,v3=punch_speed, vr1=UNSET, vr2=UNSET, vr3=UNSET)
    
    m.parts['Material'].setElementType(
        elemTypes=(
            ElemType(
                elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF,
                kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT,
                distortionControl=DEFAULT, elemDeletion=OFF, maxDegradation=0.95), 
            ElemType(elemCode=C3D6, elemLibrary=EXPLICIT), 
            ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)), 
        regions=(m.parts['Material'].cells.getSequenceFromMask(('[#1 ]',), ), )) #elemDeletion ON or OFF
    m.rootAssembly.regenerate()
    
    #Generating Finer Local Mesh
    m.parts['Material'].deleteMesh(regions=m.parts['Material'].cells.getSequenceFromMask(('[#1 ]', ), ))
    m.ConstrainedSketch(gridSpacing=0.07, name='__profile__', sheetSize=2.82, 
        transform=m.parts['Material'].MakeSketchTransform(
        sketchPlane=m.parts['Material'].faces[0], sketchPlaneSide=SIDE1, 
        sketchUpEdge=m.parts['Material'].edges[2], sketchOrientation=RIGHT, origin=(0.016, 0.0, 0.5)))
    m.parts['Material'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=m.sketches['__profile__'])
    m.sketches['__profile__'].Spot(point=(0.0, 0.0))
    m.sketches['__profile__'].FixedConstraint(entity=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(-0.21, 0.0875), point1=(-0.1225, -0.0525))
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[5], 
        entity2=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(-0.175, 0.175), point1=(0.2275, -0.1925))
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[7], 
        entity2=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].CircleByCenterPerimeter(center=(-0.1925, 0.245), point1=(0.0525, 0.0175))
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[9], 
        entity2=m.sketches['__profile__'].vertices[4])
    m.sketches['__profile__'].setAsConstruction(objectList=(
        m.sketches['__profile__'].geometry[6], 
        m.sketches['__profile__'].geometry[7], 
        m.sketches['__profile__'].geometry[8]))
    m.sketches['__profile__'].rectangle(point1=(-0.105, 0.127401923062408), point2=(0.07, -0.0875))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[11], 
        entity2=m.sketches['__profile__'].geometry[6])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[13], 
        entity2=m.sketches['__profile__'].geometry[6])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[12], 
        entity2=m.sketches['__profile__'].geometry[6])
    m.sketches['__profile__'].rectangle(point1=(-0.14, 0.303613652525705), point2=(0.186216681801385, -0.277677146014723))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[15], 
        entity2=m.sketches['__profile__'].geometry[8])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[17], 
        entity2=m.sketches['__profile__'].geometry[8])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[18], 
        entity2=m.sketches['__profile__'].geometry[8])
    m.sketches['__profile__'].rectangle(point1=(-0.325048073367618, 0.4375), point2=(0.3675, -0.4025))
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[19], 
        entity2=m.sketches['__profile__'].geometry[7])
    m.sketches['__profile__'].CoincidentConstraint(addUndoState=False, 
        entity1=m.sketches['__profile__'].vertices[21], 
        entity2=m.sketches['__profile__'].geometry[7])
    m.sketches['__profile__'].CoincidentConstraint(
        entity1=m.sketches['__profile__'].vertices[22], 
        entity2=m.sketches['__profile__'].geometry[7])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.0648780465126038, -0.0128048658370972), value=0.2, 
        vertex1=m.sketches['__profile__'].vertices[11], 
        vertex2=m.sketches['__profile__'].vertices[12])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.0187804698944092, 0.190365791320801), value=0.13, 
        vertex1=m.sketches['__profile__'].vertices[14], 
        vertex2=m.sketches['__profile__'].vertices[11])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.203170716762543, -0.0435365736484528), value=0.25, 
        vertex1=m.sketches['__profile__'].vertices[15], 
        vertex2=m.sketches['__profile__'].vertices[16])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(0.0512194633483887, 0.251829206943512), value=0.1875, 
        vertex1=m.sketches['__profile__'].vertices[18], 
        vertex2=m.sketches['__profile__'].vertices[15])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.377317011356354, 0.0913414359092712), value=0.3, 
        vertex1=m.sketches['__profile__'].vertices[19], 
        vertex2=m.sketches['__profile__'].vertices[20])
    m.sketches['__profile__'].ObliqueDimension(
        textPoint=(-0.192926824092865, 0.345731675624847), value=0.23, 
        vertex1=m.sketches['__profile__'].vertices[22], 
        vertex2=m.sketches['__profile__'].vertices[19])
    m.parts['Material'].PartitionFaceBySketch(
        faces=m.parts['Material'].faces.getSequenceFromMask(('[#1 ]', ), ), 
        sketch=m.sketches['__profile__'], sketchUpEdge=m.parts['Material'].edges[2])
    del m.sketches['__profile__']
    m.parts['Material'].regenerate()
    m.rootAssembly.regenerate()
    
    m.parts['Material'].seedEdgeBySize(
        constraint=FINER, deviationFactor=0.1, 
        edges=m.parts['Material'].edges.getSequenceFromMask(('[#7e000f ]', ), ), minSizeFactor=0.1, size=0.1) #0.1
    m.parts['Material'].seedEdgeBySize(
        constraint=FINER, deviationFactor=0.1, 
        edges=m.parts['Material'].edges.getSequenceFromMask(('[#f0f0 ]', ), ), minSizeFactor=0.1, size=0.04) #0.04
    #0.008 make this smaller for high-fidelity simulation (finer mesh)
    m.parts['Material'].seedEdgeBySize(
        constraint=FINER, deviationFactor=0.1, 
        edges=m.parts['Material'].edges.getSequenceFromMask(('[#f00 ]', ), ), minSizeFactor=0.1, size=0.008) 

    m.parts['Material'].generateMesh()
    m.parts['Material'].regenerate()
    m.rootAssembly.regenerate()
    
    #Move punch and die closer. 0.015" apart. Modify time so that material is deformed 0.050"
    m.rootAssembly.translate(instanceList=('Guide-1', ), vector=(0.0, 0.0, -0.07))
    m.rootAssembly.translate(instanceList=('Punch-1', ), vector=(0.0, 0.0, -0.05))
    m.rootAssembly.translate(instanceList=('Material-1', ), vector=(0.0, 0.0, -0.020))
        
    m.rootAssembly.regenerate()
    
    m.fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 'PEEQVAVG', 'LE', 'U', 'V', 'A', 
        'RF', 'CSTRESS', 'SDEG', 'DMICRT', 'EVF', 'COORD', 'STATUS'))
    
    job = mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
        description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
        numCpus=1, numDomains=1, numThreadsPerMpiProcess=1, queue=None, 
        resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
        0, waitMinutes=0)
    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()
    
    print(f'{i_padded} {job_name} Completed.')
    return i


# run simulations
i = 0
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        punch_clearance = float(row['punch_clearance'])
        punch_speed = float(row['punch_speed'])
        material_thickness = float(row['material_thickness'])
        i = RunSimulation(i, punch_clearance, punch_speed, material_thickness)