# Testing Strategy

## Overview
Testing focused on verifying the correctness of calculator operations and the interaction between the CLI and calculator logic.

## Unit Testing
- **What was tested:** Each arithmetic operation (addition, subtraction, multiplication, division), edge cases (division by zero, negative numbers, decimals, large numbers).  
- **What was not tested:** User interface formatting, input validation beyond basic operator checks.  
- **Rationale:** Unit tests isolate logic to ensure correctness without the complexity of user input.

## Integration Testing
- **Tests included:** 
    1. Addition flow (5 + 3 → 8)  
    2. Clear function resets result  
    3. Subtraction flow (10 - 4 → 6)  
- **Purpose:** Verify that CLI and calculator logic interact correctly and produce expected results.

## Lecture Concepts Applied
- **Testing Pyramid:** Most tests are unit tests (base of the pyramid), while integration tests are fewer (middle layer).  
- **Black-box vs White-box:** Unit tests use **white-box** testing (knowledge of Calculator methods); integration tests use **black-box** testing (simulate user interaction without relying on internal logic).  
- **Functional vs Non-Functional Testing:** Functional tests verify operations and clear functionality. Non-functional aspects like UI appearance were not tested.  
- **Regression Testing:** Running this test suite ensures that future changes do not break existing functionality.

## Test Results Summary
| Test Name | Type | Status |
|-----------|------|--------|
| test_add | Unit | Pass |
| test_subtract | Unit | Pass |
| test_multiply | Unit | Pass |
| test_divide | Unit | Pass |
| test_divide_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_addition_flow | Integration | Pass |
| test_clear_function | Integration | Pass |
| test_subtraction_flow | Integration | Pass |
