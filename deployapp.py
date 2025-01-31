from metaflow import FlowSpec, step, card, current, pypi, app_deploy, Config
import importlib

# This flow deploys a package defined in appconfig.toml as an endpoint
# You can modify this flow to fit your needs
class DeployAppFlow(FlowSpec):
    config = Config("config", default="appconfig.toml", parser="tomllib.loads")

    @app_deploy(app_name=config.app, app_port=config.port)
    @pypi(packages=config.dependencies)
    @step
    def start(self):
        try:
            mod = importlib.import_module(f"{self.config.app}.app_init")
            print("app_init module found")
        except:
            print("app_init not found, deploying without data")
            mod = None
        if mod:
            mod.init(self.deploy_dir)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    DeployAppFlow()
