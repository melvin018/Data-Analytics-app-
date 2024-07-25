import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))


from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'mean' in results
    assert results['mean'] > 0
