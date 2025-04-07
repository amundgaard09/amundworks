
import math

while True:

    #input module
    known_side = input("known side:")
    side_value = float(input("side length:"))
    angle_a = float(input("angle a:"))
    angle_b = float(input("angle b:"))
    angle_c = float(input("angle c:"))

    #complete triangle analysis function from angles
    def ctaa(angle_a,angle_b,angle_c,known_side,side_value):

        #computer
        rada = math.radians(angle_a)
        radb = math.radians(angle_b)
        radc = math.radians(angle_c)
        sina = math.sin(rada)
        sinb = math.sin(radb)
        sinc = math.sin(radc)
        cosa = math.cos(rada)
        cosb = math.cos(radb)
        cosc = math.cos(radc)
        tana = math.tan(rada)
        tanb = math.tan(radb)
        tanc = math.tan(radc)

        if known_side == 'a':
            side_a = side_value
            side_b = (side_a * sinb) / sina
            side_c = (side_a * sinc) / sina
        
        elif known_side == 'b':
            side_b = side_value
            side_a = (side_b * sina) / sinb
            side_c = (side_b * sinc) / sinb

        elif known_side == 'c':
            side_c = side_value
            side_a = (side_c * sina) / sinc
            side_b = (side_c * sinb) / sinc
        
        area = (1/2) * side_a * side_b * sinc

        #printer
        print(f"sines: a:{sina}, b:{sinb}, c:{sinc}")
        print(f"cosines: a:{cosa}, b:{cosb}, c:{cosc}")
        print(f"tangents: a:{tana}, b:{tanb}, c:{tanc}")
        print(f"sides: a:{side_a}, b:{side_b}, c:{side_c}")
        print(f"area:{area}")

        return side_a, side_b, side_c 
    side_a, side_b, side_c = ctaa(angle_a,angle_b,angle_c,known_side,side_value)