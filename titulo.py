# Datos con los que vas a trabajar
# name = "Moon"
# gravity = 0.00162 # in kms
# planet = "Earth"
borderBottom = '-' * 55
planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

title = f"""
Datos curiosos sobre {name}.
{borderBottom}
Planet name: {planet}.
Gravity in {name}: {gravity * 1000} m/s2
"""

print(title)