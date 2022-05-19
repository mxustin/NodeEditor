from dynaconf import Dynaconf as Conf

conf = Conf(envvar_prefix=False, settings_files=['settings.toml', '.secrets.toml'])
