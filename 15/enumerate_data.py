names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    # breakpoint()
    # change to one long \n delimited string to test pytest capfd vs capsys
    out = ''
    for enumerated_names in enumerate(names, 1):
        index = enumerated_names[0]
        row = (f"{index}. "
               f"{enumerated_names[1]:<11}"
               f"{countries[index - 1]}\n")

        out += row
    print(out)
