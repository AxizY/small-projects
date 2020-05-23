//login
login()

//extra stuff
function lalert(log) {
	console.log(log)
	alert(log)
}	
//login part
function login(account) {

right = false

function quiz() {

if (right == true) return;

var testuser = prompt('Username?', 'Username');

var testpass = prompt('Password?', 'Password');


if(testpass == testuser.password) {
lalert('Logged In!')
right = true

} else {
lalert('Wrong Password')



}
}
quiz()

}

//account definer
class account {
	constructor(username, password) {
	this.password = password
	this.username = username
}
}
//create account
function newaccount(username, password) {
window[username] = new account(username, password)
}

//changelogin
function changelogin(account) {
var testknownuser = prompt('Old Username?', 'Username');
if(testknownuser = account.username) {
var testknownpass = prompt('Old Password?', 'Password');
if(testknownpass == account.password) {
account.username = prompt('New Username', 'Username')
account.password = prompt('New Password', 'Password');
}}}
//clear
clear()

//login
login()
