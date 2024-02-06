side = int(input("Enter the length of the side of a cube: "))

def cube_measurements(side):
    surfaceArea = 6 * (side**2)
    volume = side**3

    
    return surfaceArea, volume
    
surfaceArea,volume = cube_measurements(side)
print(f"Surface area: {surfaceArea}     Volume: {volume}")
