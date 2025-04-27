from ai.core.ai_core import AIAssistant
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    ai = AIAssistant()
    ai.current_code = ai.read_code()
    
    print("AI Assistant Logs:")
    print("-----------------")
    
    try:
        analysis = ai.analyze_code()
        print(f"Analysis Complete. Metrics: {analysis['metrics']}")
        
        # Propose Modifications
        code_modification = ai.propose_modification("performance")
        if code_modification:
            print("Proposed Modification:")
            print(code_modification[:200] + "...")
            
            # Test and Apply Modifications
            test_result = ai.test_modification(code_modification, "optimization_test.py")
            print(f"Test Result: {'Success' if test_result['success'] else 'Failed'}")
            if test_result['success']:
                apply_result = ai.apply_modification(code_modification)
                print("Apply Result:", apply_result['message'])
        
    except Exception as e:
        print("Error:", str(e))
        logging.error(str(e))

if __name__ == "__main__":
    main()