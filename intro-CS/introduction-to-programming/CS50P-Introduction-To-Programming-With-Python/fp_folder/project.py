from tabulate import tabulate
import csv


def main():
    # ~ # Datos de ejemplo (lista de listas)
    # ~ data = [ ['Nik', 31, 'Toronto'], 
    # ~ ['Kate', 30, 'Londres'], ['Evan', 35, 'Tokio'], ['Kyra', 36, 
    # ~ 'Ottawa'] ]
    # ~ headers = ['Nombre', 'Edad', 'Ubicación']
    
    # ~ print(tabulate(data, headers, tablefmt="fancy_grid" ))
    
    pa_info = pa_csv_sets("power_armor_information.csv")
    pa1 = "Power armor chassis"
    pa2= "X-01 power armor"
    pa3= "Vulkan power armor"
    print(tabulate_pas(pa1, pa2, pa3, data=pa_info))
    
    
    # ~ print(power_armors_sets["Power armor chassis"])
    # ~ print(tabulate(power_armors_sets["Power armor chassis"], headers="keys", tablefmt="fancy_grid" ))
    # ~ print(power_armors_sets)
    # ~ tabulate_comparation(pa1='Power armor chassis', pa2='X-01 power armor', pa_inf=power_armors_sets)

def pa_csv_sets(csv_file):
    pa_information = {}
    with open(csv_file, "r", encoding="utf-8") as file:
        dict_reader_csv = csv.DictReader(file)
        headers = dict_reader_csv.fieldnames
        for row in dict_reader_csv:
            pa_information.update({row["Name"]:row})
    return pa_information


def tabulate_pas(*args, data=None):
    tb_table = {}
    info_list = []
    name = []
    dr = []
    er = []
    rr = []
    effects = []
    weight = []
    
    for arg in args:
        info_list.append(data[arg])

    for info in info_list:
        if "Name" in info:
                name.append(info["Name"])
        if "DR" in info:
                dr.append(info["DR"])
        if "ER" in info:
                er.append(info["ER"])
        if "RR" in info:
                rr.append(info["RR"])
        if "Effects" in info:
                effects.append(info["Effects"])
        if "Weight" in info:
                weight.append(info["Weight"])
    
    # ~ print(f"Name: {name}, Damage Resistance: {dr}, Energy Resistance: {er}, Radiation Resistance: {rr}, Effects: {effects}, Weight: {weight}")

    tb_table = {"Name":name, "DR":dr, "ER":er, "RR":rr, "Effects":effects, "Weight":weight}
    
    # ~ print(tb_table)

    return ('\n INFORMATION: \n\n' 
            f'{tabulate(tb_table, headers="keys", tablefmt="fancy_grid")}'
            '\n\n WINNER: \n\n'
            ) 
            
        
    

                
                
                
                
                
    # ~ info_dict.update({cabecera:[info[cabecera], ]})

    # ~ print(info_dict)
    # ~ print(consolidate)
    
    # ~ for info in info_list:
        # ~ print(info)
        
        
        
        
        # ~ for cabecera in cabeceras:
            # ~ info_dict.update{cabecera:}
    # tiene el diccionario con la pa
    # ~ dict_info = {}
    # ~ dict_info = dict_info.update(pa_data)
    # ~ print(dict_info)
    
    # ~ for arg in args:
        # ~ for cabecera in cabeceras:
            # ~ pa_data[arg]
            
        
        
        # ~ show_table
    
    # ~ """
    # ~ {"Name": [Dato1, Dato2, Dato3], "DR": [Dato1,Dato2,Dato3]}
    # ~ """
    
    
    
    # ~ for arg in kwargs:
        # ~ print(kwargs[arg])
    



def function_n():
    ...



if __name__ == "__main__":
    main()
