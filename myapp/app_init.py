import os
import json
from metaflow import Flow


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
