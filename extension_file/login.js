
window.onload = function(){
	    var userN = document.getElementById('submit')

		
	    userN.addEventListener('click',function(){
			var username = document.getElementById('username').value;
			var pw = document.getElementById('password').value;
			var path = document.getElementById('save_path').value;
			chrome.runtime.sendMessage({"username":username,"password":pw,"save_path":path});
		});
		
}

