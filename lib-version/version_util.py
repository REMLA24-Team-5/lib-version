from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    @staticmethod
    def get_version():
        package_name = "lib-version"
        try:
            return version(package_name)
        except PackageNotFoundError:
            return "Package not found"
        return version

# Example usage
if __name__ == "__main__":
    version = VersionUtil.get_version()
    print("Library version:", version)