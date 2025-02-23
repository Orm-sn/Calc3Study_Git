import random as rd
import numpy as np


def sub_menu_11_7():
    selection = int(input("Select what to practice from this module (type number only): \n"
                          "1. Spherical coordinates to rectangular conversion: \n"
                          "2. Cylindrical coordinates to rectangular conversion: \n"
                          "3. Equation find for cylindrical coord to rectangular coord: \n"
                          "4. Equation find for spherical coordinates to rectangular coord: \n"
                          "5. Exit section 11.7: \n" or 5))

    match selection:
        case 1:
            spherical_coord_conversion()
        case 2:
            cylinder_coord_conversion()
        case 3:
            return
        case 4:
            return
        case 5:
            return


def spherical_coord_conversion():
    margin = 0.5
    p = rd.randint(1, 20)
    theta_int = rd.randint(1, 10)
    theta = np.pi / theta_int
    phi_int = rd.randint(1, 10)
    phi = np.pi / phi_int

    print(f"Convert the following point from spherical coordinates to rectangular coordinates: "
          f"({p},π/{theta_int},π/{phi_int}) \n")
    ans_x = round(float(input("Input your x value as decimal: " or 1)), 2)
    ans_y = round(float(input("Input your y value as decimal: " or 1)), 2)
    ans_z = round(float(input("Input your z value as decimal: " or 1)), 2)
    x = round(p * np.sin(phi) * np.cos(theta), 2)
    y = round(p * np.sin(phi) * np.sin(theta), 2)
    z = round(p * np.cos(phi))
    if abs(ans_x - x) <= margin and abs(ans_y - y) <= margin and abs(ans_z - z) <= margin:
        print("Correct!")
        return
    else:
        print(f"X expected {round(x, 2)} received {ans_x} Y expected {round(y, 2)} received {ans_y} "
              f"Z expected {round(z, 2)} received {ans_z}")
        print("First of all do you agree that the formula is x = p*sin(Φ)*cos(Θ) \n"
              "and y = p*sin(Φ)*sin(Θ) \n"
              "and z = p*cos(Φ)?\n")

    spherical_coord_conversion()


def cylinder_coord_conversion():
    margin = 0.5
    r = rd.randint(1, 20)
    theta_int = rd.randint(1, 10)
    theta = np.pi / theta_int
    z = rd.randint(1, 20)

    print(f"Convert the following point from cylindrical coordinates to rectangular coordinates: "
          f"({r},π/{theta_int},{z}) \n")
    ans_x = round(float(input("Input your x value as decimal: " or 1)), 2)
    ans_y = round(float(input("Input your y value as decimal: " or 1)), 2)
    ans_z = float(input("Input your z value as decimal: " or 1))
    x = round(r * np.cos(theta), 2)
    y = round(r * np.sin(theta), 2)

    if abs(ans_x - x) <= margin and abs(ans_y - y) <= margin and abs(ans_z - z) <= margin:
        print("Correct!")
        return
    else:
        print(f"X expected {round(x, 2)} received {ans_x} Y expected {round(y, 2)} received {ans_y} "
              f"Z expected {round(z, 2)} received {ans_z}")
        print("First of all do you agree that the formula is x = r*cos(Θ) \n"
              "and y = r*sin(Θ) \n"
              "and z = z?")
    cylinder_coord_conversion()


def cylinder_coord_equation():
    return


def spherical_coord_equation():
    return
