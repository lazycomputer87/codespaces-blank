import os
import json
from ai.tools import code_analyzer, code_generator
from ai.ml.models import code_analyzer_model

class AIAssistant:
    def __init__(self):
        self.objectives = [
            "maintain_code_integrity",
            "debug_code",
            "test_modifications",
            "optimize_performance"
        ]
        self.current_code = self.read_code()
        self.sandbox = Sandbox()
        self.ml_model = code_analyzer_model.load_model()

    def read_code(self):
        with open(__file__, "r") as f:
            return f.read()

    def analyze_code(self):
        analysis = code_analyzer.analyze(self.current_code)
        analysis["model_score"] = self.ml_model.predict(analysis["metrics"])
        return analysis

    def propose_modification(self, modification_type):
        analysis = self.analyze_code()
        if modification_type == "performance":
            return code_generator.optimize_code(self.current_code, analysis)
        elif modification_type == "debug":
            return code_generator.fix_bugs(self.current_code, analysis)
        return None

    def test_modification(self, modified_code, file_name):
        return self.sandbox.run_test(modified_code, file_name)

    def apply_modification(self, modified_code):
        test_result = self.test_modification(modified_code, "temp_code.py")
        if test_result["success"]:
            with open(__file__, "w") as f:
                f.write(modified_code)
            return {"status": "success", "message": "Modification applied."}
        return {"status": "error", "message": "Modification failed."}