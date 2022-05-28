# simpleATMcontroller
A simple ATM controller designed for assessment purposes. As required by the design specification, functions, classes, and methods are implemented. This program can be extended by adding interfaces. 
# Installation
<strong>Step 1:</strong> Download the source from the terminal:
<pre><code>git clone https://github.com/junhb/simpleATMcontroller
</code></pre>
<strong>Step 2:</strong> Execute the program:
<pre><code>python3 app.py
</code></pre>
# Code Design
The structure of the program is divided into three main parts.
## <code>Bank</code> class
<ul>
  <li>The constructor initializes <code>data</code> for storing all the user information.</li>
  <li><code>add_user</code> function adds users to <code>data</code>. The ID, name, card number, and PIN of the user should be passed for initialization. <code>Accounts</code> is initialized for storing different types of accounts (e.g. savings, checking, etc.) </li>
  <li><code>add_account</code> function adds accounts for users. The type of the account and the initial balance should be passed. The balance can be changed so that the balance is 0 if an initial deposit is not made.</li>
  <li><code>get_id</code> function returns the <code>user_id</code> when the card number is passed.</li>
  <li><code>check_pin</code> function returns <code>True</code> if the PIN matches that in the system. Otherwise, <code>False</code> is returned. </li>
  <li><code>get_accounts</code> function returns all the accounts owned by the user</li>
</ul>

## <code>ATMController</code> class

<ul>
   <li> The constructor initializes the following variables. The user's bank is assigned to the <code>Bank</code>. <code>cash_bin</code> models the cash bin of a real-world ATM. <code>cash_bin</code> is built for future purposes (e.g. interfaces). The ID of the owner of the card is assigned to <code>user_id</code>. The list of accounts owned by a user e.g. Savings, Checking, etc. is assigned to <code>accounts</code>. The account selected by the user is assigned to <code>account</code>. </li>
  <li> <code>insert_card</code> function checks whether the card number is in <code>data</code> </li>
  <li> <code>insert_pin</code> function checks whether the PIN typed by the user matches the PIN in the system. If the PIN typed by the user matches that in the system, the list of user accounts is assigned to <code>accounts</code>.</li>
  <li> <code>select_account</code> function passes the account selected by the user. The selected account is assigned to <code>account</code> variable.</li>
  <li> <code>see_balance</code> function returns the remaining balance. </li>
  <li> <code>deposit</code> function adds the cash inserted in <code>cash_bin</code> to the account selected by the user.</li>
  <li> <code>withdraw</code> function subtracts the amount of cash typed by the user from the remaining balance. If the user intends to cash out more than the amount remaining in the balance, the transaction is rejected. </li>
</ul>

## <code>main</code> function
The main function will run a few test cases using the <code>assert</code> statements. 
<ul>
  <li> <code>sys.exit()</code> is called if the Python version is lower than 3.10.2 </li> 
  <li> Few hypothetical users are added to <code>test_bank</code>, with <code>user_id</code>, <code>user_name</code>, <code>card_num</code>. </li>
  <li> Few cards are thought to be inserted into the <code>test_atm</code>. This is done by passing their card numbers. The program returns <code>True</code> if the card number exists in the bank <code>data</code>. <code>False</code> is returned if the card number does not exist in <code>data</code>. </li>
  <li> Correct PINs and wrong PINs are passed for testing purposes. </li>
  <li> Existing accounts and non-existing accounts are passed for testing purposes. </li>
  <li> <code>see_balance</code>, <code>deposit</code>, <code>withdraw</code> functions are tested. </li>
  <li> The test prints "Everything passed" if all sanity checks are done.</li>
  <li> More test cases can be added to the <code>main</code> function.</li>
</ul>
