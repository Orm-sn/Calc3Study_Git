# Import files from other parts of the project (different problem types)
import Section11_7


def menu():
    selection = int(input("Menu options: select practice problem type or escape to exit program (type number only): \n"
                          "Option 1: Section 11.7 Practice: \n"
                          "Option 2: Section 12.1 Practice: \n"
                          "Option 3: Section 12.2 Practice: \n"
                          "Option 4: Section 12.3 Practice: \n"
                          "Option 5: Section 12.4 Practice: \n"
                          "Option 6: Section 12.5 Practice: \n"
                          "Option 7: section 13.1 Practice: \n"
                          "Option 8: Section 13.2 Practice: \n"
                          "Option 9: Section 13.3 Practice: \n"
                          "Option 10: Section 13.4 Practice: \n"
                          "Option 11: Section 13.5 Practice: \n"
                          "12 to exit: \n" or 12))

    # Switch statement to select from case
    match selection:
        case 1:
            Section11_7.sub_menu_11_7()
            return "cont"
        case 2:
            return "cont"
        case 3:
            return
        case 4:
            return
        case 5:
            return
        case 6:
            return
        case 7:
            return
        case 8:
            return
        case 9:
            return
        case 10:
            return
        case 11:
            return
        case 12:
            return


while menu() == "cont":
    menu()
