from core import *

dimYear = Dimension("Year")
dimYear.elements.add("2022")
dimYear.elements.add("2023")
dimYear.elements.add("2024")
dimYear.elements.add("2025")

dimPeriod = Dimension("Period")
dimPeriod.elements.add(['Total Year', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])

dimUnit = Dimension("Unit")
dimUnit.elements.add(["All Units", "VIE1", "MUC1", "BER2"])

dimAccount = Dimension("Account")
dimAccount.elements.add(["Room Nights", "Average Room Rate", "Revenue"])

cube = Cube("Market Segments")
cube.dimensions.add([dimYear, dimPeriod, dimUnit, dimAccount])
cube.compile()

print(cube.dimensions[-2].name)

for d in cube.dimensions:
    print("{0}: Elements = {1}".format(d.name, d.elements.count()))

cube.write_value(100, ["2022", "01", "MUC1", "Room Nights"])
