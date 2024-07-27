*** Settings ***
Library    ../resources/books_keywords.py

*** Variables ***
${BOOK_NAME}               The Lord of the Rings
${AUTHOR}                  J.R.R. Tolkien
${ISBN}                    9785171358136
${PAGE_COUNT}              1120
${USER_1}                  Vasya
${USER_2}                  Petya

*** Test Cases ***
Test Reserve Book
    [Documentation]    Test reserving a book that is not busy or reserved.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user}=    Create User Instance    ${USER_1}
    ${result}=    Reserve Book    ${book}    ${user}
    Should Be True    ${result}
    ${result}=    Reserve Book    ${book}    ${user}
    Should Be Equal As Strings    ${result}    reserved
    Log    Sucsessfully reserving a book

Test Borrow Book
    [Documentation]    Test borrowing a book that is reserved by the user.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user}=    Create User Instance    ${USER_1}
    ${result}=    Reserve Book    ${book}    ${user}
    Should Be True    ${result}
    ${result}=    Borrow Book    ${book}    ${user}
    Should Be True    ${result}
    Log    Sucsessfully borrowing a book

Test Borrow Book Reserved By Another User
    [Documentation]    Test trying to borrow a book that is reserved by another user.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user1}=    Create User Instance    ${USER_1}
    ${user2}=    Create User Instance    ${USER_2}
    ${result}=    Reserve Book    ${book}    ${user1}
    Should Be True    ${result}
    ${result}=    Borrow Book    ${book}    ${user2}
    Should Be Equal As Strings    ${result}    reserved_by_other
    Log    Book reserved by another user

Test Return Book
    [Documentation]    Test returning a book that was borrowed.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user}=    Create User Instance    ${USER_1}
    ${result}=    Borrow Book    ${book}    ${user}
    Should Be True    ${result}
    ${result}=    Return Book    ${book}
    Should Be Equal As Strings    ${result}    returned
    Log    Sucsessfully returning a book

Test Cancel Reservation
    [Documentation]    Test canceling a reservation of a book.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user}=    Create User Instance    ${USER_1}
    ${result}=    Reserve Book    ${book}    ${user}
    Should Be True    ${result}
    ${result}=    Return Book    ${book}
    Should Be Equal As Strings    ${result}    reserve_cancelled
    Log    Sucsessfully canceling a reservation a book

Test Reserve And Borrow
    [Documentation]    Test reserving and then borrowing a book.
    ${book}=    Create Book Instance    ${BOOK_NAME}    ${AUTHOR}    ${ISBN}    ${PAGE_COUNT}
    ${user1}=    Create User Instance    ${USER_1}
    ${user2}=    Create User Instance    ${USER_2}
    ${result}=    Reserve Book    ${book}    ${user1}
    Should Be True    ${result}
    ${result}=    Borrow Book    ${book}    ${user1}
    Should Be True    ${result}
    ${result}=    Borrow Book    ${book}    ${user2}
    Should Be Equal As Strings    ${result}    taken
    Log    Sucsessfully reserving and then borrowing a book
