# simpleATMcontroller
A simple ATM controller designed for assessment purpose. Only functions, classes, and methods are implemented to be within the scope of the design requirements.
# Installation
<strong>Step 1:</strong> Download the source from the terminal
<pre><code>git clone https://github.com/junhb/simpleATMcontroller
</code></pre>
<strong>Step 2:</strong> Execute the program:
<pre><code>python3 app.py
</code></pre>
# Code Design
The structure of the program is divided into three main parts.
## <code>Bank</code> class
<ul>
  <li>The constructor is initiallized with <code>data</code> dictionary for storing all the details of users as</li>
  <li><code>add_user</code> function adds users to <code>data</code>. The user id, name, card number, pin should be passed for initiation. <code>Accounts</code> key is initialized to store different kinds of accounts (e.g.) Savings, Checking, etc.) </li>
  <li><code>add_account</code> function to add accounts for users. The type of the account and the initial balance should be passed. The balance can be changed so that the balance is 0 if initial deposit is not made. However, this is not within the scope of this project</li>
  <li><code>add_account</code> function to verify whether the info of the user of the inserted card is in the bank <code>data</code> </li>
  <li><code>get_id</code> function returns the <code>user_id</code> when the card number is passed</li>
  <li><code>check_pin</code> function returns <code>True</code> if the pin number matches the user info. Otherwise, <code>False</code> is returned. </li>
  <li><code>get_accounts</code> function returns the accounts owned by a user</li>
  <li><code>get_accounts</code> function returns the accounts owned by a user</li>
</ul>

## <code>ATMController</code> class

<ul>
   <li></li>
</ul>
