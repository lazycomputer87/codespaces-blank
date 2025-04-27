import subprocess
import os

class Sandbox:
    def __init__(self):
        self.sandbox_dir = os.path.join(os.getcwd(), "sandbox")
        if not os.path.exists(self.sandbox_dir):
            os.makedirs(self.sandbox_dir)

    def run_test(self, code, file_name):
        file_path = os.path.join(self.sandbox_dir, file_name)
        try:
            with open(file_path, "w") as f:
                f.write(code)
            result = subprocess.run(
                ["python", file_path],
                cwd=self.sandbox_dir,
                capture_output=True,
                text=True,
                timeout=5
            )
            return {
                "success": True,
                "output": result.stdout,
                "error": result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def clean_up(self):
        for file in os.listdir(self.sandbox_dir):
            file_path = os.path.join(self.sandbox_dir, file)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")