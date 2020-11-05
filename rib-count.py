#!/usr/bin/env python
# import providers, services and models
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ip_rib_ipv4_oper as xr_ip_rib_ipv4_oper
import logging


if __name__ == "__main__":
    """Main execution path"""


    #logger = logging.getLogger("ydk")
    #logger.setLevel(logging.INFO)
    #handler = logging.StreamHandler()
    #formatter = logging.Formatter(("%(asctime)s - %(name)s - "
    #                            "%(levelname)s - %(message)s"))
    #handler.setFormatter(formatter)
    #logger.addHandler(handler)


# create NETCONF session
    provider = NetconfServiceProvider(address="10.85.171.230",
                                      port=830,
                                      username="cisco",
                                      password="cisco",
                                      protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    # create rib_limit object
    rib_limit = xr_ip_rib_ipv4_oper.Rib()

    # read rib from device
    rib_limit = crud.read(provider, rib_limit)

    # Define variables
    lim = int(rib_limit.rib_table_ids.rib_table_id["e0000001"].information.conf_prefix_limit)
    cnt = int(rib_limit.rib_table_ids.rib_table_id["e0000001"].information.current_prefix_count)
    vrf = str(rib_limit.rib_table_ids.rib_table_id["e0000001"].information.vrf_name)
    pcnt = 100*(cnt/lim)

    # Print rib informtion
   
    print(f"Prefix limit for vrf {vrf} is {lim}")
    print(f"Prefix count for vrf {vrf} is {cnt}")
    print(f"Prefix limit utilization for vrf {vrf}: {pcnt}%")


    exit()
