import math

aMasses = [
	54172,
	58469,
	92948,
	143402,
	57563,
	54532,
	68042,
	89847,
	70872,
	54069,
	107310,
	146439,
	88851,
	142869,
	71309,
	89613,
	70338,
	87708,
	95305,
	134384,
	128250,
	134991,
	91270,
	127819,
	68650,
	102556,
	129882,
	68688,
	129939,
	137344,
	102624,
	90828,
	86487,
	91712,
	114866,
	75697,
	107599,
	99053,
	87511,
	128128,
	57772,
	69314,
	90771,
	145376,
	100730,
	142675,
	112731,
	83985,
	123565,
	127325,
	86597,
	121772,
	131992,
	148859,
	93348,
	77294,
	119763,
	74636,
	95592,
	79628,
	78861,
	68565,
	88820,
	134291,
	69262,
	128678,
	118216,
	52799,
	92731,
	61600,
	63477,
	64016,
	131872,
	131412,
	146579,
	104400,
	99110,
	63458,
	144393,
	54787,
	148622,
	91323,
	61137,
	106082,
	103644,
	63795,
	126648,
	61489,
	140964,
	110963,
	72696,
	124370,
	110466,
	139317,
	108440,
	148062,
	89992,
	145645,
	70556,
	95739,
]

def get_fuel_mass(iMass):
	# take its mass, divide by three, round down, and subtract 2.
	return int(math.floor(iMass/float(3))) - 2

def recursive_get_fuel_mass(iMass):
	iFuel = get_fuel_mass(iMass)
	if iFuel <= 0:
		return 0
	else:
		return iFuel + recursive_get_fuel_mass(iFuel)

iTotal = 0;
for iMass in aMasses:
	iTotal += get_fuel_mass(iMass)

print "Part 1: " + str(iTotal)

iTotal = 0;
for iMass in aMasses:
	iFuel = recursive_get_fuel_mass(iMass)
	iTotal += iFuel

print "Part 2: " + str(iTotal)