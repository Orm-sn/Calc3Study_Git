import streamlit as st
import random as rd
import numpy as np


def section_11_7():
    st.header("Section 11.7 - Practice Problems")

    # Selection Menu
    problem_type = st.radio("Select what to practice:", [
        "Spherical to Rectangular Conversion",
        "Cylindrical to Rectangular Conversion",
        "Equation Find for Cylindrical to Rectangular",
        "Equation Find for Spherical to Rectangular",
    ])

    match problem_type:
        case "Spherical to Rectangular Conversion":
            spherical_coord_conversion()
        case "Cylindrical to Rectangular Conversion":
            cylinder_coord_conversion()
        case "Equation Find for Cylindrical to Rectangular":
            equation_cylinder_rectangular()
        case "Equation Find for Spherical to Rectangular":
            equation_spherical_to_rectangular()
        case _:
            st.write("This section is under development.")


def spherical_coord_conversion():
    st.subheader("Spherical to Rectangular Conversion")
    margin = 0.5
    if "spherical_params" not in st.session_state or st.button("Generate New Problem"):
        st.session_state.spherical_params = {
            "p": rd.randint(1, 20),
            "theta_int": rd.randint(1, 10),
            "phi_int": rd.randint(1, 10)
        }

    p = st.session_state.spherical_params["p"]
    theta_int = st.session_state.spherical_params["theta_int"]
    phi_int = st.session_state.spherical_params["phi_int"]
    theta = np.pi / theta_int
    phi = np.pi / phi_int

    st.write(
        f"Convert the following point from spherical to rectangular coordinates: ({p}, π/{theta_int}, π/{phi_int})")

    ans_x = st.number_input("Enter your x value:", step=0.01)
    ans_y = st.number_input("Enter your y value:", step=0.01)
    ans_z = st.number_input("Enter your z value:", step=0.01)

    if st.button("Submit Answer"):
        x = round(p * np.sin(phi) * np.cos(theta), 2)
        y = round(p * np.sin(phi) * np.sin(theta), 2)
        z = round(p * np.cos(phi), 2)

        if abs(ans_x - x) <= margin and abs(ans_y - y) <= margin and abs(ans_z - z) <= margin:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Expected: x={x}, y={y}, z={z}, but received x={ans_x}, y={ans_y}, z={ans_z}")
            st.write("Hint: Use the formulas:")
            st.latex(r"x = p \sin(\phi) \cos(\theta)")
            st.latex(r"y = p \sin(\phi) \sin(\theta)")
            st.latex(r"z = p \cos(\phi)")


def cylinder_coord_conversion():
    st.subheader("Cylindrical to Rectangular Conversion")
    margin = 0.5
    if "cylinder_params" not in st.session_state or st.button("Generate New Problem"):
        st.session_state.cylinder_params = {
            "r": rd.randint(1, 20),
            "theta_int": rd.randint(1, 10),
            "z": rd.randint(1, 20)
        }

    r = st.session_state.cylinder_params["r"]
    theta_int = st.session_state.cylinder_params["theta_int"]
    z = st.session_state.cylinder_params["z"]
    theta = np.pi / theta_int

    st.write(f"Convert the following point from cylindrical to rectangular coordinates: ({r}, π/{theta_int}, {z})")

    ans_x = st.number_input("Enter your x value:", step=0.01)
    ans_y = st.number_input("Enter your y value:", step=0.01)
    ans_z = st.number_input("Enter your z value:", step=0.01)

    if st.button("Submit Answer"):
        x = round(r * np.cos(theta), 2)
        y = round(r * np.sin(theta), 2)

        if abs(ans_x - x) <= margin and abs(ans_y - y) <= margin and abs(ans_z - z) <= margin:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Expected: x={x}, y={y}, z={z}, but received x={ans_x}, y={ans_y}, z={ans_z}")
            st.write("Hint: Use the formulas:")
            st.latex(r"x = r \cos(\theta)")
            st.latex(r"y = r \sin(\theta)")
            st.latex(r"z = z")


def equation_cylinder_rectangular():
    if "problem_type_equation_cylinder" not in st.session_state:
        st.session_state.problem_type_equation_cylinder = rd.randint(1, 2)

        # Button to generate a new problem type
    if st.button("Generate New Problem"):
        st.session_state.problem_type_equation_cylinder = rd.randint(1, 2)

        # Call the correct function based on stored problem type
    if st.session_state.problem_type_equation_cylinder == 1:
        rec_to_cyl()
    else:
        cyl_to_rec()


def rec_to_cyl():
    if "rec_equation_params" not in st.session_state:
        st.session_state.rec_equation_params = {
            "constant": rd.randint(1, 20),
        }
    constant = st.session_state.rec_equation_params["constant"]
    st.subheader("Rectangular to Cylindrical Coordinate Equation")
    st.write("Find an equation in cylindrical coordinates for the equation given in rectangular coordinates")
    st.latex(fr"z = x^2 + y^2 + {constant}")
    ans = st.text_input("Answer: ", key="rec_to_cyl_answer")
    if st.button("Submit Answer", key="rec_to_cyl_submit"):
        if ans.lower().strip() == f"z = r^2 + {constant}":
            st.success("Correct!")
            del st.session_state.rec_equation_params
        else:
            st.error(f"Remember it should look like z = r^2 + {constant}")


def cyl_to_rec():
    if "cyl_equation_params" not in st.session_state:
        st.session_state.cyl_equation_params = {
            "r": rd.randint(1, 10)
        }
    r = st.session_state.cyl_equation_params["r"]
    st.subheader("Rectangular to Cylindrical Coordinate Equation")
    st.write("Find an equation in rectangular coordinates for the equation given in cylindrical coordinates")
    st.latex(fr"r = {r}")
    ans = st.text_input("Answer: ", key="cyl_to_rec_answer")
    if st.button("Submit Answer", key="cyl_to_rec_submit"):
        if ans.lower().strip() == f"x^2+y^2={r ** 2}":
            st.success("Correct!")
            del st.session_state.cyl_equation_params
        else:
            st.error("Did you remember to square r?")


def equation_spherical_to_rectangular():
    if "equation_spherical_to_rec" not in st.session_state:
        st.session_state.equation_spherical_to_rec = {
            "problem_type": rd.randint(1, 3)
        }

    if st.button("Generate New Problem"):
        st.session_state.equation_spherical_to_rec["problem_type"] = rd.randint(1, 2)

    problem_type = st.session_state.equation_spherical_to_rec["problem_type"]
    match problem_type:
        case 1:
            sph_to_rec_row()
        case 2:
            rec_to_sph()


def sph_to_rec_row():
    if "sph_equations_rho" not in st.session_state:
        st.session_state.sph_equations_rho = {
            "rho": rd.randint(1, 20)
        }
    rho = st.session_state.sph_equations_rho["rho"]
    st.subheader("Spherical to rectangular")
    st.write("Find an equation in rectangular coordinates for the equation given in spherical coordinates")
    st.latex(fr"\rho = {rho}")
    ans = st.text_input("Answer: ")
    if st.button("Submit Answer"):
        if ans.lower().strip() == f"x^2+y^2+z^2={rho ** 2}":
            st.success("Correct!")
            del st.session_state.sph_equations_rho
        else:
            st.error("Did you remember to square rho?")


def rec_to_sph():
    return
