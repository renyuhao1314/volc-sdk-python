# coding:utf-8
from __future__ import print_function

from volcengine.bioos.BioOsService import BioOsService

if __name__ == '__main__':
    bioos_service = BioOsService(endpoint="endpoint")

    # call below method if you don't set ak and sk in $HOME/.volc/config
    bioos_service.set_ak('ak')
    bioos_service.set_sk('sk')

    params = {}

    resp = bioos_service.list_workspaces(params)
    print(resp)

