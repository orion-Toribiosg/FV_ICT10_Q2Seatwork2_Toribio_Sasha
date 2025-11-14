from js import document
from pyscript import display 

def general_weighted_average(e):
    first_name = document.getElementById("input1").value
    last_name = document.getElementById("input2").value
    science = float(document.getElementById('input3').value)
    math = float(document.getElementById('input4').value)
    english = float(document.getElementById('input5').value)
    filipino = float(document.getElementById('input6').value)
    ict = float(document.getElementById('input7').value)
    pe = float(document.getElementById('input8').value)

    #as used in the guidelines/guide, this part below is the calculation of the grades/numbers in the input values from the main html file
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1) #this part is for units (how much each subject contributes to the gwa)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE'] #list type
    summary = f"""
    {subjects[0]}: {science:.2f}
    {subjects[1]}: {math:.2f}
    {subjects[2]}: {english:.2f}
    {subjects[3]}: {filipino:.2f}
    {subjects[4]}: {ict:.2f}
    {subjects[5]}: {pe:.2f}
        """
    #part where code is transmitted when button is pressed; all of the code above is calculated here below 
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
