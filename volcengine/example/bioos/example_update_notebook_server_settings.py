# coding:utf-8
from __future__ import print_function

from volcengine.bioos.BioOsService import BioOsService

if __name__ == '__main__':
    # set endpoint/region here if the default value is unsatisfied
    bioos_service = BioOsService(endpoint='endpoint', region='region')

    # call below method if you don't set ak and sk in $HOME/.volc/config
    bioos_service.set_ak('ak')
    bioos_service.set_sk('sk')

    params = {
        "WorkspaceID": "workspace_id",
        "ResourceSize": "small",
        "ImageID": "1",
        "MountTOSEnabled": False,
        "TempImageName": "jupyter/minimal-notebook"
    }

    resp = bioos_service.update_notebook_server_settings(params)
    print(resp)
