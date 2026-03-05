\# Testing Strategy



\## Overview

Testing focused on verifying the correctness of calculator operations and the interaction between the CLI and calculator logic.



\## Unit Testing

\- \*\*What was tested:\*\* Each arithmetic operation (addition, subtraction, multiplication, division), edge cases (division by zero, negative numbers, decimals, large numbers).  

\- \*\*What was not tested:\*\* User interface formatting, input validation beyond basic operator checks.  

\- \*\*Rationale:\*\* Unit tests isolate logic to ensure correctness without the complexity of user input.



\## Integration Testing

\- \*\*Tests included:\*\* 

&nbsp;   1. Addition flow (5 + 3 → 8)  

&nbsp;   2. Clear function resets result  

&nbsp;   3. Subtraction flow (10 - 4 → 6)  

\- \*\*Purpose:\*\* Verify that CLI and calculator logic interact correctly and produce expected results.



\## Lecture Concepts Applied

\- \*\*Testing Pyramid:\*\* Most tests are unit tests (base of the pyramid), while integration tests are fewer (middle layer).  

\- \*\*Black-box vs White-box:\*\* Unit tests use \*\*white-box\*\* testing (knowledge of Calculator methods); integration tests use \*\*black-box\*\* testing (simulate user interaction without relying on internal logic).  

\- \*\*Functional vs Non-Functional Testing:\*\* Functional tests verify operations and clear functionality. Non-functional aspects like UI appearance were not tested.  

\- \*\*Regression Testing:\*\* Running this test suite ensures that future changes do not break existing functionality.



\## Test Results Summary

| Test Name | Type | Status |

|-----------|------|--------|

| test\_add | Unit | Pass |

| test\_subtract | Unit | Pass |

| test\_multiply | Unit | Pass |

| test\_divide | Unit | Pass |

| test\_divide\_by\_zero | Unit | Pass |

| test\_negative\_numbers | Unit | Pass |

| test\_decimal\_numbers | Unit | Pass |

| test\_large\_numbers | Unit | Pass |

| test\_addition\_flow | Integration | Pass |

| test\_clear\_function | Integration | Pass |

| test\_subtraction\_flow | Integration | Pass |

