import sys
import os

# Add the parent directory of the module to the sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
print(f"Adding {module_path} to sys.path")
sys.path.insert(0, module_path)


from consolesink import ConsoleSink

def test_sink_data(capfd, dict):
    dict = {'key': 'value'}
    ConsoleSink().sink_data(dict)
    captured = capfd.readouterr()
    assert captured.out == str(dict) + '\n'
    
    