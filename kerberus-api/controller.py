import sys
from models import *
    
def main(args):
    order = kerberus_api.get_orders()
    x_tid = '<http://napsao-qa-nix-croupier-workflow-3.qa.vmcommerce.intra:8080/v1/riskanalysis/51233695?statusHash=51233678OWR1446568786036>; method="post"; secret="eb943a18972bddd7d814530e98f3e4d1c5ec0b9e"'
    header = { "Content-Type" :  "application/json", "X-Callback" : x_tid }
    url = args[1]
    user = args[2]
    passworld = args[3]
    # print(url + ' ' + user + ' ' + passworld)
    kapi = kerberus_api(url, user, passworld)
    kapi.create_order(order, header)

if __name__ == '__main__' : 
    main(sys.argv)