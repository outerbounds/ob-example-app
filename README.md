
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

You can access the API in any environment that has a valid Outerbounds access token installed, either
associated with a user or a machine token. For starters, you can test this on the workstation:

- Install a simple auth wrapper library: `pip install -U outerbounds-app-client`

- Run
```
python client_example.py https://api...
```
replacing the argument with the API URL output by the deployment flow. If you see a JSON output, you
can access the endpoint programmatically from any authenticated environment! 🎉

