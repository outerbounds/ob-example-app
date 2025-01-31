import os
import json
from metaflow import Flow

# This function is called at the deploy time to populate
# any data (artifacts) to be served by the endpoint. Serialize
# any data you want to serve in `deploy_dir`, provided as an
# argument.
#
# Typically, you would use the Metaflow Client API to access
# artifacts produced by other flows here
def init(deploy_dir):
    try:
        model = Flow("ScalableFlow").latest_successful_run.data.best
        print("ScalableFlow model found!")
    except:
        print("ScalableFlow model not found")
        model = None
    if model:
        with open(os.path.join(deploy_dir, "data.json"), "w") as f:
            json.dump({"model": model}, f)
