


def Valve_specs(SelectedValve):
    """
    This module retrieves GLV specs from valdata.csv for the selected gas lift valve model.
    """
    #By Alex, August 2012
    #valdata.csv file is CSV file that contains GL valve specifications. 
    #It was created with Excel from Comprehensive_Gas_Lift_valve_specs.xlsx
    #which in turn is used in all Excel-based gas lift related modules written by Nick.
    # Argument (SelectedValve) is string containing the GL valve model
    
    Psz=[]      # float - (in/64), list of valve port sizes
    
    fp=[]       # float - (-), list of valve port factors clumsily called TEF in g/l literature = R/(1-R),  R=Ap/Ab
    
    fodpp=[]    # float - (psi) list of pressure increases over Ppc (production closing pressure) required to fully open the gas lift valve
                # it is derivad from GLV load rate and it is used for the dynamic valve performance calculations.
                # for details see Nick's gas lift seminar material
    
    All_valves = open("valdata.csv",'r')
    
    found = False
    for line in All_valves: 
        line = line.rstrip()
        line = line.split(',')
        if line[1] == SelectedValve:
            Manuf = line[0]
            Type = line[5]
            Tsens = line[6]
            Psz.append(float(line[2]))     
            fp.append(float(line[3]+"0"))        #concatenates  "0"   so float conversion does not blow up for orifice where fp = '' (null) 
            fodpp.append(float(line[4]+".0"))    #concatenates  ".0"  so float conversion does not blow up for orifice where fodpp = '' (null)
            found = True
        elif found == True:
            break;
    All_valves.close() 
    
    if not found:
        print ("Valve %s not found") % (SelectedValve)
    else:          
        n_ports = len(Psz)
        # This block is just to test the results
        def displayResults(fs):
            fs.write("{:10s}  {:10s}  {:10s} {:10s} {:10s}\n".format('Model','NPsz','Manuf','Type','Tsensitive'))
            fs.write("{:10s}  {:<10d}  {:10s} {:10s} {:10s}\n".format(SelectedValve, n_ports, Manuf,Type,Tsens))
            
            fs.write("\nPort sizes............: ")
            for port in Psz:
                fs.write("{:<8.0f}".format(port))
            fs.write("\nPort factors..........: ")
            for fpp in fp:
                fs.write("{:<8.3f}".format(fpp))
            fs.write("\ndP to fully open......: ")
            for dppfo in fodpp:
                fs.write("{:<8.0f}".format(dppfo))             
        
        import sys
        fs = sys.stderr 
        displayResults(fs)
  
        fs = open("found_specs.txt", 'w')
        displayResults(fs)   
        fs.close()   

def main():
    #SelectedValve = 'AT1-STD-BK'
    SelectedValve = 'R-20'    
    Valve_specs(SelectedValve)
    
    #both instructions below blow up.  How to access Psz[], fp[] and fodpp[] ?
    print Valve_specs.fp
    print "\n\nFourth port factor is {:<8.3f}".format(Valve_specs.fp[3])
    #Or even better: how to modify  Valve_specs() so it returns Psz[], fp[] and fodpp[]?
    #If only one list is calculated e.g. Psz[] then perhaps teh statement return Psz would do the trick ?
if __name__ == "__main__":
    main()