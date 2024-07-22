*** Settings ***
Library    bank_keywords.py

*** Variables ***
${VALID_CUSTOMER_NAME}      Lionel Messi
${INVALID_CUSTOMER_NAME}    L!0n3l M3ss!
${VALID_DEPOSIT_AMOUNT}     1000
${VALID_PERIOD}             12
${VALID_RATE}               5
${INVALID_DEPOSIT_AMOUNT}   -1000
${ZERO_DEPOSIT_AMOUNT}      0
${EMPTY}                    ''

*** Test Cases ***
Positive Test Case: Calculate Monthly Capitalization
    [Documentation]    Test for calculating monthly capitalization with valid data.
    ${deposit_amount}=    ${VALID_DEPOSIT_AMOUNT}
    ${period}=    ${VALID_PERIOD}
    ${rate}=    ${VALID_RATE}
    ${bank}=    Create Bank Instance    ${deposit_amount}    ${period}    ${rate}
    ${result}=    Calculate Monthly Capitalization    ${bank}
    Should Be Equal As Numbers    ${result}    1051.16

Negative Test Case: Negative Deposit Amount
    [Documentation]    Test for creating a bank instance with a negative deposit amount.
    ${deposit_amount}=    ${INVALID_DEPOSIT_AMOUNT}
    ${period}=    ${VALID_PERIOD}
    ${rate}=    ${VALID_RATE}
    Run Keyword And Expect Error    ValueError    Create Bank Instance    ${deposit_amount}    ${period}    ${rate}

Boundary Test Case: Zero Deposit Amount
    [Documentation]    Test for creating a bank instance with a zero deposit amount.
    ${deposit_amount}=    ${ZERO_DEPOSIT_AMOUNT}
    ${period}=    ${VALID_PERIOD}
    ${rate}=    ${VALID_RATE}
    ${bank}=    Create Bank Instance    ${deposit_amount}    ${period}    ${rate}
    ${result}=    Calculate Monthly Capitalization    ${bank}
    Should Be Equal As Numbers    ${result}    0

Customer Test Case: Valid Name
    [Documentation]    Test for creating a customer with a valid name.
    ${customer}=    Create Customer Instance    ${VALID_CUSTOMER_NAME}
    Should Be Equal    ${customer.name}    ${VALID_CUSTOMER_NAME}

Negative Test Case: Invalid Customer Name
    [Documentation]    Test for creating a customer with an invalid name.
    ${name}=    ${INVALID_CUSTOMER_NAME}
    Run Keyword And Expect Error    ValueError    Create Customer Instance    ${name}

Empty Name Customer Test Case: Empty Name
    [Documentation]    Test for creating a customer with an empty name.
    ${name}=    ${EMPTY}
    Run Keyword And Expect Error    ValueError    Create Customer Instance    ${EMPTY}
