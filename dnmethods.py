import sys
import dnfile
import argparse



def usage():
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description = "Dump methods from a C# portable executable file.")
    parser.add_argument("path", metavar="filepath", type=str, help="path of the C# PE file")
    parser.add_argument("options", metavar="options", type=str, help="what to dump (t: class, m: methods, p: parameters, f: fields)", default="tmpf")
    args = parser.parse_args()
    
    pe = dnfile.dnPE(args.path)

    if "t" in args.options:
        for typerow in pe.net.mdtables.TypeDef:
            print("Class \"" + typerow.TypeName + "\":")
            if "m" in args.options:
                print("Methods:")
                for methodrow in typerow.MethodList:
                    print("\t" + methodrow.row.Name)
                    if "p" in args.options:
                        print("\t\tParameters:")
                        for paramrow in methodrow.row.ParamList:
                            print("\t\t\t" + paramrow.row.Name)
                            if "f" in args.options:
                                print("Fields:")
                                for fieldrow in typerow.FieldList:
                                    print("\t" + fieldrow.row.Name)
    
if __name__ == "__main__":
    main()
