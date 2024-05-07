import subprocess

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            # Run git describe with subprocess to get the latest tag
            git_version = subprocess.check_output(['git', 'describe', '--tags']).strip().decode('utf-8')
            # Format the output to only return the tag part
            version = git_version.split('-')[0]
        except Exception:
            version = 'unknown'
        return version

# Example usage
if __name__ == "__main__":
    version = VersionUtil.get_version()
    print("Library version:", version)