class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance._config_data = {}
        return cls.__instance

    def __del__(self):
        Config.__instance = None

    def set_config(self, key, value):
        self._config_data[key] = value

    def get_config(self, key):
        return self._config_data.get(key)


if __name__ == "__main__":
    config1 = Config()
    config1.set_config("language", "English")
    print(config1.get_config("language"))

    config2 = Config()
    config2.set_config("theme", "Dark")
    print(config2.get_config("theme"))

    print(config1.get_config("theme"))
