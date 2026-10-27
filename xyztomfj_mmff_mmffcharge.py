import sys

# usuage: python xyztomfj_mmff_mmffcharge.py input.xyz charge.key output.mfj
# this program reads in the .xyz and .key file from sdf2tinkerxyz program for mmff atomtype and charge assignment

# import argument variables
try:
 txyzin = sys.argv[1]
except:
 print("""
 ERROR!!
 usuage: python xyztomfj_mmff_mmffcharge.py input.xyz charge.key output.mfj

 """)

try:
 keyin = sys.argv[2]
except:
 print("""
 ERROR!!
 usuage: python xyztomfj_mmff_mmffcharge.py input.xyz charge.key output.mfj

 """) 

try:
 mfjout = sys.argv[3]
except:
 print("""
 ERROR!!
 usuage: python xyztomfj_mmff_mmffcharge.py input.xyz charge.key output.mfj

 """)

#open files
txyzin = open(txyzin,"r")
print("\nSuccessfully opened the input xyz file...\n")

keyin = open(keyin,"r")
print("Successfully opened the input key file...\n")

mfjout = open(mfjout,"w")
print("Successfully opened the output file for writing...\n")

#open mass and vdw param files. their names are by default mass.prm and vdw.prm
massin = open("mass.prm","r")
print("Successfully opened the input mass.prm file...\n")

vdwin = open("vdw.prm","r")
print("Successfully opened the input vdw.prm file...\n")


#read the txyz file and obatin the atom number
txyzlines = txyzin.readlines()
atomnum = int((txyzlines[0].split()[0]))

#summarize the atom info in txyz
info1 = []
for i in range(1,1+atomnum):
 info1.append(txyzlines[i].split())

print("Starting to read the txyz file...\n")
print("Number of atoms from the txyz file: " + str(atomnum) + "\n")

#print the read information for checking
#print("Atom information read from the txyz file: \n")
#for i in range(atomnum):
# print(info1[i])

#read the key file containing the charges
keylines = keyin.readlines()

print("Starting to read the key file...\n")

#summarize the atom info in the key file
info2 = []
for i in range(0,atomnum):
 info2.append(keylines[i].split())

#print the read information for checking
#print("Atom information read from the key file: \n")
#for i in range(atomnum):
# print(info2[i])


print("\nReading in mass info...\n")

mass = massin.readlines()

#read mass info and generate an atom type mass dictionary. Assumes that the total entry (line number) is 212
atinfo = {}

for i in range(212):
 atinfo[(mass[i].split())[1]] = (mass[i].split())[2]

#generate a mass dictionary. Assumes that the total entry (line number) is 212
minfo = {}

for i in range(212):
 minfo[(mass[i].split())[2]] = (mass[i].split())[6]
 print(str((mass[i].split())[2] + "," + str((mass[i].split())[6]) + "\n"))

#read vdw info and generate a dictionary. Assumes that the total entry (line number) is 95
print("Reading in vdw info...\n")

vdw = vdwin.readlines()
vinfo = {}

for i in range(95):
 vinfo[(vdw[i].split())[0]] = [(vdw[i].split())[1],(vdw[i].split())[2],(vdw[i].split())[3],(vdw[i].split())[4]]


#start writing the mfj file:

inputname = ((sys.argv[3]).split("."))[0]

print("\nWriting basic information to the output file...")
mfjout.write(inputname + "\n")
mfjout.write("1\n")
mfjout.write(str(atomnum) + "\n")
mfjout.write("ang\n")
mfjout.write("calc\n")
mfjout.write("1.0000\n")

#Write atom information
print("Writing atom information to the output file...\n")

#coordinates, from the txyz file(info1)
for i in range(atomnum):
 mfjout.write(info1[i][2] + " " + info1[i][3] + " " + info1[i][4])

#mass
#info1[i][5] is the atomtype info in the txyz file
 try:
  mfjout.write(" " + str(minfo[atinfo[info1[i][5]]]))
 except:
  print("\n\n\nERROR!!\n\n\n")
  print("No mass for atom type " + atinfo[info1[i][5]])

#charge
#info2[i][8] is the charge info in the key file
 mfjout.write(" " + info2[i][2])
 
#vdw
#info1[i][5] is the atomtype info in the txyz file
 try:
  mfjout.write(" " + vinfo[atinfo[info1[i][5]]][0] + " " + vinfo[atinfo[info1[i][5]]][1] + " " + vinfo[atinfo[info1[i][5]]][2] + " " + vinfo[atinfo[info1[i][5]]][3] + "\n" )
 except:
  print("\n\n\nERROR!!\n\n\n")
  print("No vdw parameters for atom number " + info1[i][5])

print("\n Writing Completed!")
print(" Always double-check your output")

#Calculate the total charge for user convenience

charge = 0
mass = 0

for i in range(atomnum):
 charge += float(info2[i][2])
 mass += float(minfo[atinfo[info1[i][5]]])
 
print("\n For your information: ")
print(" Sum of Atomic Charges = " +  str(charge) + "\n")
print(" Sum of Atomic masses = " +  str(mass) + "\n")
