import toml

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            # Read version from pyproject.toml
            with open('pyproject.toml', 'r') as file:
                pyproject_toml = toml.load(file)
                version = pyproject_toml['tool']['poetry']['version']
        except (FileNotFoundError, KeyError):
            version = 'unknown'
        return version

# Example usage
if __name__ == "__main__":
    version = VersionUtil.get_version()
    print("Library version:", version)