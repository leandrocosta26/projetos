import csv
import sys

f = open(sys.argv[1], 'rt')
fobj_out = open("out.txt", "w+")
i = 0
try:
    reader = csv.reader(f)
    for row in reader:
        p_ped = row[3]
        vl_final = row[5]
        p_id_item = row[9]
        vl_meio = row[7]
        vl_unit = row[10]
        temp = ''
        if p_ped != '':
            if i > 0 :
                if vl_final not in '0' : 
                    temp+= "UPDATE IMPORTACAO_PEDIDO_CLIENTE SET P_VL_FINAL='{vl_final}' WHERE P_PED_CLIENTE='{p_ped}'\n ".format(vl_final=vl_final, p_ped=p_ped)
                if p_id_item not in '' and vl_unit not in '0' : 
                    temp+= "UPDATE IMPORTACAO_PEDIDO_ITEM P_VL_UNITARIO='{vl_unit}' WHERE P_PED_CLIENTE='{p_ped}' AND P_ID_ITEM='{p_id_item}'\n".format(vl_unit=vl_unit,p_ped=p_ped, p_id_item=p_id_item)
                if vl_meio not in '0': 
                    temp+= "UPDATE IMPORTACAO_PEDIDO_MEIO_PAGAMENTO SET P_VL_MEIO='{vl_meio}' WHERE P_PED_CLIENTE='{p_ped}'\n".format(vl_meio=vl_meio,p_ped=p_ped)
                    
                fobj_out.write(temp)
        i+=1
        
finally:
    f.close()
    fobj_out.close()