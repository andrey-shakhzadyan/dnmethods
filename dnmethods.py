import sys
import dnfile


def main():
    path = sys.argv[1]
    if len(sys.argv) == 3:
        options = sys.argv[2]
    else:
        options = "tmpf"

        pe = dnfile.dnPE(path)

        if "t" in options:
            for typerow in pe.net.mdtables.TypeDef:
                print("Class \"" + typerow.TypeName + "\":")
                if "m" in options:
                    print("Methods:")
                    for methodrow in typerow.MethodList:
                        print("\t" + methodrow.row.Name)
                        if "p" in options:
                            print("\t\tParameters:")
                            for paramrow in methodrow.row.ParamList:
                                print("\t\t\t" + paramrow.row.Name)
                    
                                if "f" in options:
                                    print("Fields:")
                                    for fieldrow in typerow.FieldList:
                                        print("\t" + fieldrow.row.Name)
    
if __name__ == "__main__":
    main()
