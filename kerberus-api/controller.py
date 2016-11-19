import sys
import pdb
from models import *

def main():
    for a in range(450,100000):
        order = kerberus_api.get_orders()
        callback = "<http://napsao-qa-nix-croupier-workflow-3.qa.vmcommerce.intra:8080/v1/riskanalysis/"+ str(a) + "?statusHash=51233678OWR1446568786036>; method=\"post\"; secret=\"eb943a18972bddd7d814530e98f3e4d1c5ec0b9e\""
        header = { "Content-Type" :  "application/json", "X-Callback" : callback }
        url = "http://localhost:8080/orders/"
        user = "services"
        passworld = "123456"
        order = order.replace("51233650", str(a))
        # print(url + ' ' + user + ' ' + passworld)
        kapi = kerberus_api(url, user, passworld)
        #pdb.set_trace()
        kapi.create_order(order, header)

if __name__ == '__main__' :
    main()
