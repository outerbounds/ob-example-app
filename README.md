
# Template for deploying apps and endpoints on Outerbounds

## Quickstart

1. Start a new workstation using the following image:
```
006988687827.dkr.ecr.us-west-2.amazonaws.com/obp-apps/vanilla:master-81c04052-1738296769
```

2. Clone this repo on the workstation
```
git clone https://github.com/outerbounds/ob-example-app.git
```

3. Deploy an example app
```
cd ob-example-app
./deployapp
```
It will output two URLs:
- A browser URL prefixed with `https://ui.`
- An API URL prefixed with `https://api.`

Click the browser URL to test the endpoint in the browser. If you see a JSON output, your endpoint works! 🎉

5. Test API access

You can access your freshly deployed endpoint in any environment that has a valid Outerbounds access token
installed, either associated with a user or a machine token. For starters, you can test it on the workstation:

- Install a simple auth wrapper library: `pip install -U outerbounds-app-client`

- Run
```
python client_example.py https://api...
```
replacing the argument with the API URL output by the deployment flow. If you see a JSON output, you
can access the endpoint programmatically from any authenticated environment! 🎉

To access the endpoint in another (micro)service, you should mint a new **machine user** for
programmatic access, [following the instructions here](https://docs.outerbounds.com/outerbounds/machine-users/).

> [!TIP]
> Reach out to your support Slack if you need help configuring machine users

## Developing your own apps and endpoints

Your endpoint needs to be implemented as a Python package, such as `myapp` included here as an example.
Your endpoint package can implement a Streamlit app, a FastAPI server, or any other service that
serves HTTP requests at a given port.

Your package needs to implement an entrypoint script at `__main__.py` which starts the server.
Importantly, the server needs to start at a `port` defined in `appconfig.toml`, which also specifes
the package to be deployed with the `app` key.

List any Python (Pypi) dependencies that your service requires in the `[dependencies]` section
in `appconfig.toml`. These libraries are installed automatically during deployment.

## Serving models and other data through endpoints

You can expose any data, Metaflow artifacts in particular, to your deployments. For instance,
you can deploy the latest model produced by a separate training flow, stored as an artifact.

To load arbitrary data in your deployments, implement a `app_init` module in your package.
This module needs to include a method
```
def init(deploy_dir):
    ...
```
which is called at **deploy time** to make any data available for your endpoint. Typically,
this method uses Metaflow client to retrieve artifacts and store them in the given `deploy_dir`
so they are accessible by the deployment.

To see this in action, run [the `ScalableFlow` example in the Getting Started 
section](https://docs.outerbounds.com/outerbounds/first-scale/). The flow will produce a dummy
model, stored as an artifact `best`. Deploy `myapp` again to invoke `myapp.app_init`
which loads the artifact and serves it through the endpoint.