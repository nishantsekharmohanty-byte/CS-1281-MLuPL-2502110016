
def run_tests():
    print("\nHOSTILE INPUT TEST")
    print("=" * 45)

    test_cases = [
        ("WO01 | Machine A | Normal operation", True),
        ("WO02|Machine B|Completed", True),
        ("WO03   |   Machine C   | Running", True),
        ("XX04 | Machine D | Normal", False),
        ("WO05 | Machine E", False),
        ("WO06 | ??? | NULL", False),
        ("WO07 | Machine G | ERROR: Failure", False),
        ("WO08 | Machine H | Pressure HIGHHIGHHIGH", False),
        ("", False),
        ("WO09 | | Missing machine", False)
    ]

    passed = 0
    failed = 0

    for test_input, expected in test_cases:

        record, reason = parse_record(test_input)

        actual = record is not None

        if actual == expected:
            print("[PASS]", repr(test_input))
            passed += 1
        else:
            print("[FAIL]", repr(test_input))
            print("Expected:", expected)
            print("Actual:", actual)
            failed += 1

    print("\nTEST RESULTS")
    print("Passed:", passed)
    print("Failed:", failed)

    if failed == 0:
        print("ALL TESTS PASSED")
    else:
        print("SOME TESTS FAILED")

    return failed == 0

SHIFT LOG REPORT
======================================================================
WORK ORDER     MACHINE             STATUS
----------------------------------------------------------------------
WO01           Machine A           Normal operation
WO02           Machine B           Maintenance completed
WO03           Machine C           Inspection passed
WO04           Machine A           Temperature stable
WO05           Machine B           Filter replaced
WO06           Machine C           Running normally
WO07           Machine D           Inspection completed
WO09           Machine D           Inspection passed
WO10           Machine A           Operating normally
WO11           Machine B           Oil level checked
WO12           Machine C           Maintenance required
WO13           Machine D           Shift completed

MACHINE SUMMARY
-----------------------------------
Machine A                    3
Machine B                    3
Machine C                    3
Machine D                    3

TOTALS
Records processed: 15
Accepted records: 12
Rejected records: 3
